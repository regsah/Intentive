import subprocess
import os

UTILS_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(UTILS_DIR)
BACKEND_DIR = os.path.dirname(APP_DIR)
APPS_DIR = os.path.dirname(BACKEND_DIR)
ROOT_DIR = os.path.dirname(APPS_DIR)
FFMPEG_BIN = os.path.join(ROOT_DIR, "ffmpeg", "bin", "ffmpeg.exe")

def convert_webm_to_wav(webm_path: str, wav_path: str):
    command = [
        FFMPEG_BIN,
        '-i', webm_path,
        wav_path
    ]
    subprocess.run(command, check=True)
