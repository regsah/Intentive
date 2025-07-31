from fastapi import APIRouter, HTTPException
from app.db.models import TextInput

router = APIRouter()

@router.post("/submit_text")
async def submit_text(data: TextInput):
    return {"type": "text", "content": data.text}
