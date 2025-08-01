import subprocess
import os

from app.utils.paths import FFMPEG_BIN

def convert_webm_to_wav(webm_path: str, wav_path: str):
    command = [
        FFMPEG_BIN,
        '-i', webm_path,
        wav_path
    ]
    subprocess.run(command, check=True)
