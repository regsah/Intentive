from fastapi import APIRouter, HTTPException, UploadFile, File, FastAPI
from app.db.models import TextInput

import json

router = APIRouter()

@router.post("/submit_text")
async def submit_text(data: TextInput):
    file_path = "../../local_storage/text_submissions.json"

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    new_entry = {"type": "text", "content": data.text}
    existing_data.append(new_entry)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

    return new_entry

@router.post("/submit_audio")
async def submit_audio(audio: UploadFile = File(...)):
    audio_bytes = await audio.read()

    with open(f"../../local_storage/audio/{audio.filename}", "wb") as f:
        f.write(audio_bytes)

    return {
        "type": "audio",
        "filename": audio.filename,
        "size": len(audio_bytes)
    }

