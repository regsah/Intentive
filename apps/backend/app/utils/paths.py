import os

UTILS_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(UTILS_DIR)
BACKEND_DIR = os.path.dirname(APP_DIR)
APPS_DIR = os.path.dirname(BACKEND_DIR)
ROOT_DIR = os.path.dirname(APPS_DIR)

FFMPEG_BIN = os.path.join(ROOT_DIR, "ffmpeg", "bin", "ffmpeg.exe")
LOCAL_STORAGE_DIR = os.path.join(ROOT_DIR, "local_storage")
