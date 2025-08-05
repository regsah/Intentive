from fastapi import APIRouter, HTTPException, UploadFile, File, Form, BackgroundTasks
from uuid import UUID
from app.db.models import TextInput

from app.utils.audio import process_audio
from app.services.intent_classification import classify_intent
from app.services.emotion_classification import classify_emotion

from app.db.database_scripts import add_entry, get_entries, get_intents, get_emotions, get_input_types

from app.api.helper import safe_fetch, process_audio_task, process_text_task

import os

from app.utils.paths import LOCAL_STORAGE_DIR

AUDIO_DIR = os.path.join(LOCAL_STORAGE_DIR, "audio")
TEXT_PATH = os.path.join(LOCAL_STORAGE_DIR, "text.json")    

router = APIRouter()


@router.post("/submit_text")
async def submit_text(data: TextInput, background_tasks: BackgroundTasks = None):
    background_tasks.add_task(process_text_task, data)
    return {"status": "accepted", "id": str(data.id)}

@router.post("/submit_audio")
async def submit_audio(id: UUID = Form(...), audio: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    audio_bytes = await audio.read()

    audio_path = os.path.join(AUDIO_DIR, f"{id}.webm")
    with open(audio_path, "wb") as f:
        f.write(audio_bytes)

    background_tasks.add_task(process_audio_task, id, audio_path)
    return {"status": "accepted", "id": str(id)}

@router.get("/fetch_entries")
async def fetch_entries(intent_label: str = None, emotion_label: str = None, type_label: str = None):
    try:
        entries = get_entries(intent_label=intent_label, emotion_label=emotion_label, type_label=type_label)
        return {"status": "success", "data": entries}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/fetch_type_label")
async def fetch_type_label():
    return safe_fetch(get_input_types)

@router.get("/fetch_intent_label")
async def fetch_intent_label():
    return safe_fetch(get_intents)

@router.get("/fetch_emotion_label")
async def fetch_emotion_label():
    return safe_fetch(get_emotions)
