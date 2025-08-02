import subprocess
import os

from app.utils.paths import FFMPEG_BIN

def convert_audio_type(prev_path: str, next_path: str):
    command = [ FFMPEG_BIN, '-i', prev_path, next_path ]
    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {prev_path} to {next_path}: {e}")
