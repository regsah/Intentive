from fastapi import APIRouter, HTTPException, UploadFile, File, FastAPI, Form
from uuid import UUID
from app.db.models import TextInput
from app.services.speech_to_text import transcribe_audio
from app.utils.local_store import save_data
from app.utils.audio import convert_webm_to_wav

import json
import os

# This is temporary storage for text submissions
# until a proper database is set up.
API_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(API_DIR)
BACKEND_DIR = os.path.dirname(APP_DIR)
APPS_DIR = os.path.dirname(BACKEND_DIR)
ROOT_DIR = os.path.dirname(APPS_DIR)
LOCAL_STORAGE_DIR = os.path.join(ROOT_DIR, "local_storage")
AUDIO_DIR = os.path.join(LOCAL_STORAGE_DIR, "audio")
TEXT_PATH = os.path.join(LOCAL_STORAGE_DIR, "text.json")    

router = APIRouter()


@router.post("/submit_text")
async def submit_text(data: TextInput):
    new_entry = {"id": str(data.id), "type": "text", "content": data.text}
    save_data(TEXT_PATH, new_entry)
    
    return {"status": "success", "data": new_entry}


@router.post("/submit_audio")
async def submit_audio(id: UUID = Form(...), audio: UploadFile = File(...)):
    audio_bytes = await audio.read()

    audio_path = os.path.join(AUDIO_DIR, f"{id}.webm")
    with open(audio_path, "wb") as f:
        f.write(audio_bytes)

    convert_webm_to_wav(audio_path, audio_path.replace(".webm", ".wav"))
    os.remove(audio_path)
    audio_path = audio_path.replace(".webm", ".wav")

    try:
        transcription = transcribe_audio(audio_path, "tr")
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))

    new_entry = {
        "id": str(id),
        "type": "audio",
        "filename": audio.filename,
        "size": len(audio_bytes),
        "content": transcription,
    }
    save_data(TEXT_PATH, new_entry)

    return {
        "status": "success",
        "data": {
            "id": str(id),
            "type": "audio",
            "filename": audio.filename,
            "size": len(audio_bytes),
            "content": transcription
        }
    }


