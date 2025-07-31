import whisper
import os

model = whisper.load_model("base")

def transcribe_audio(file_path: str, language: str = None) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    result = model.transcribe(file_path, language=language)
    return result["text"]
