import whisper
import os
import subprocess
from pydub import AudioSegment
import time

def ms_to_srt_time(ms):
    """Convert milliseconds to SRT time format hh:mm:ss,ms"""
    sec, ms = divmod(ms, 1000)
    min, sec = divmod(sec, 60)
    hr, min = divmod(min, 60)
    return f"{hr:02}:{min:02}:{sec:02},{ms:03}"

def convert_to_mp4(input_path, output_path):
    command = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-strict", "experimental",
        output_path
    ]
    subprocess.run(command)

def extract_audio_from_video(video_path, audio_output_path):
    command = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-q:a", "0",
        "-map", "a",
        audio_output_path,
        "-y"
    ]
    subprocess.run(command)

def generate_srt(audio, model):
    subtitles = []
    start_time = 0
    end_time = 0
    chunk_length = 3000  # Length of each audio chunk in milliseconds

    for i in range(0, len(audio), chunk_length):
        chunk = audio[i:i + chunk_length]
        
        temp_filename = "temp_chunk.mp3"
        chunk.export(temp_filename, format="mp3")
        
        result = model.transcribe(temp_filename)
        transcribed_text = result["text"]
        
        os.remove(temp_filename)
        
        end_time = start_time + len(chunk)
        
        subtitles.append({
            'start_time': ms_to_srt_time(start_time),
            'end_time': ms_to_srt_time(end_time),
            'text': transcribed_text
        })
        
        start_time = end_time

    with open("subtitles.srt", "w") as f:
        count = 1
        for subtitle in subtitles:
            f.write(f"{count}\n")
            f.write(f"{subtitle['start_time']} --> {subtitle['end_time']}\n")
            f.write(f"{subtitle['text']}\n\n")
            count += 1

def burn_subtitles_to_video(video_path, srt_path, output_path):
    command = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-vf", f"subtitles={srt_path}",
        "-c:a", "copy",
        output_path
    ]
    subprocess.run(command)

if __name__ == "__main__":
    start_time = time.time()
    input_video_path = "test.mp4"
    converted_video_path = "converted_video.mp4"
    audio_output_path = "extracted_audio.mp3"
    
    # Convert to MP4
    convert_to_mp4(input_video_path, converted_video_path)
    
    # Extract audio from converted video
    extract_audio_from_video(converted_video_path, audio_output_path)
    
    # Load the extracted audio file
    audio = AudioSegment.from_file(audio_output_path, format="mp3")
    
    # Initialize Whisper model
    model = whisper.load_model("small")
    
    # Generate SRT
    generate_srt(audio, model)
    
    # Burn subtitles into the converted video
    burn_subtitles_to_video(converted_video_path, "subtitles.srt", "output_video_with_subtitles.mp4")
    # end time
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    # remove temp files
    os.remove(converted_video_path)
    os.remove(audio_output_path)

