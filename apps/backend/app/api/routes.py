from fastapi import APIRouter, HTTPException, UploadFile, File, FastAPI, Form
from uuid import UUID
from app.db.models import TextInput
from app.utils.local_store import save_data
from app.utils.audio import process_audio

import os

from app.utils.paths import LOCAL_STORAGE_DIR

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

    transcription = process_audio(audio_path, "tr")

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
        "data": new_entry
    }


