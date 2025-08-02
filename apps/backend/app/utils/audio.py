import subprocess
import os
from fastapi import HTTPException

from app.utils.paths import FFMPEG_BIN
from app.services.speech_to_text import transcribe_audio

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
        raise HTTPException(status_code=500, detail=f"Error converting {file_path} to {new_file_path}: {e}")

    try:
        os.remove(file_path)
    except OSError as e:
        raise HTTPException(status_code=500, detail=f"Error deleting file {file_path}: {e}")
    
    return new_file_path

def process_audio(file_path: str, language: str = "tr") -> str:
    audio_path = update_audio_type(file_path, "wav")

    try:
        transcription = transcribe_audio(audio_path, language)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")
    
    return transcription