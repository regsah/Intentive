import subprocess
import os

from app.utils.paths import FFMPEG_BIN

def convert_audio_type(prev_path: str, next_path: str):
    command = [ FFMPEG_BIN, '-i', prev_path, next_path ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def update_audio_type(file_path: str, new_extension: str):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")

    base, _ = os.path.splitext(file_path)
    new_file_path = f"{base}.{new_extension}"

    try:
        convert_audio_type(file_path, new_file_path)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {file_path} to {new_file_path}: {e}")
        raise

    os.remove(file_path)
    return new_file_path
