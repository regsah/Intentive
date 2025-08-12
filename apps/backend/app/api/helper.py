import os
from fastapi import HTTPException

from app.db.database import AsyncSessionLocal

from app.db.models import TextInput

async def safe_fetch(fetch_func):
    async with AsyncSessionLocal() as session:
        try:
            data = await fetch_func(session)
            return {"status": "success", "data": data}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception:
            raise HTTPException(status_code=500, detail="Internal Server Error")

async def process_entry(id, content, entry_type):
    from app.services.emotion_classification import classify_emotion
    from app.services.intent_classification import classify_intent
    from app.db.database_scripts import add_entry


    intent = await classify_intent(content)
    emotion = await classify_emotion(content)
    new_entry = {
        "id": str(id), 
        "type": entry_type, 
        "content": content, 
        "intent": intent, 
        "emotion": emotion
    }
    async with AsyncSessionLocal() as session:
        await add_entry(session, new_entry)
        await session.commit()


async def process_text_task(data: TextInput):
    await process_entry(data.id, data.text, "text")
    
async def process_audio_task(id, audio_path):
    from app.utils.audio import process_audio
    transcription = await process_audio(audio_path, "tr")
    await process_entry(id, transcription, "audio")