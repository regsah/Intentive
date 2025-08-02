import whisper
import os

from app.utils.paths import FFMPEG_BIN

local_ffmpeg_dir = os.path.dirname(FFMPEG_BIN)
os.environ["PATH"] = local_ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")

model = whisper.load_model("small")

def transcribe_audio(file_path: str, language: str = None) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    result = model.transcribe(file_path, language=language)
    return result["text"]
