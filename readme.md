# Auto-Subtitle Generator 🎬🤖

### "Because watching a video without subtitles is like eating a cake without frosting. It's possible, but why would you?" 🎂

## Overview

Are you tired of manually transcribing your videos? So are we! This Auto-Subtitle Generator uses the mythical power of `ffmpeg` and `Whisper` to automatically generate and burn subtitles into your videos.

## What Does This Script Do? 🤔

1. **Converts a video to MP4 format**: Because we like to keep it mainstream.
2. **Extracts audio from the video**: We're like the audio FBI.
3. **Transcribes the audio to text**: Like your personal secretary, but less awkward.
4. **Generates an SRT file**: No, not a Dodge car model. SRT as in "SubRip Text."
5. **Burns the subtitles into the video**: Hotter than your mixtape. 🔥

## Installation & Dependencies 🛠️

### "I've got 99 problems, but dependency ain't one."

First, make sure you have Python 3.x installed. If you don't, download it [here](https://www.python.org/downloads/).

Next, install the required Python packages by running:

```bash
pip install -r requirements.txt
```

We rely on these fancy libraries:

- `Whisper` for speech-to-text
- `pydub` for audio manipulation
- `ffmpeg` for video and audio processing

**Note**: You also need to have `ffmpeg` installed. If you haven't, get it [here](https://ffmpeg.org/download.html).

## How to Use 🚀

### "It's so simple, even your grandma could do it. Well, assuming she codes in Python."

1. Place your video file (named `test.mp4`) in the project directory.
2. Run the script using the command:

```bash
python main.py
```

3. Enjoy your video complete with subtitles. It's like magic, but real.

## Troubleshooting 🚑

If you run into issues, it's not us, it's you. Just kidding! Open an issue, and we'll get back to you when we're not busy saving the world.

## Like This Project? ⭐

Give it a star! Because we love stars. Not as much as we love bugs, but we're working on that.
