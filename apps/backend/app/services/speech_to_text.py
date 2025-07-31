import whisper
import os

UTILS_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(UTILS_DIR)
BACKEND_DIR = os.path.dirname(APP_DIR)
APPS_DIR = os.path.dirname(BACKEND_DIR)
ROOT_DIR = os.path.dirname(APPS_DIR)
FFMPEG_BIN = os.path.join(ROOT_DIR, "ffmpeg", "bin", "ffmpeg.exe")

local_ffmpeg_dir = os.path.dirname(FFMPEG_BIN)
os.environ["PATH"] = local_ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")

model = whisper.load_model("base")

def transcribe_audio(file_path: str, language: str = None) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    result = model.transcribe(file_path, language=language)
    return result["text"]
