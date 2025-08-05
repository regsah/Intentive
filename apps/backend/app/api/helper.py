import os
from fastapi import HTTPException

from app.utils.audio import process_audio
from app.services.emotion_classification import classify_emotion
from app.services.intent_classification import classify_intent

from app.db.database_scripts import add_entry

from app.db.models import TextInput

def safe_fetch(fetch_func):
    try:
        return {"status": "success", "data": fetch_func()}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

def process_entry(id, content, entry_type):
    intent = classify_intent(content)
    emotion = classify_emotion(content)
    new_entry = {
        "id": str(id), 
        "type": entry_type, 
        "content": content, 
        "intent": intent, 
        "emotion": emotion
    }
    add_entry(new_entry)


def process_text_task(data: TextInput):
    process_entry(data.id, data.text, "text")
    
def process_audio_task(id, audio_path):
    transcription = process_audio(audio_path, "tr")
    process_entry(id, transcription, "audio")