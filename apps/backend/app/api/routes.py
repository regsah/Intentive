from fastapi import APIRouter, HTTPException
from app.db.models import TextInput



router = APIRouter()

@router.post("/submit_text")
async def submit_text(data: TextInput):
    with open("../../local_storage/text_submissions.txt", "a") as f:
        f.write(data.text + "\n")

    return {"type": "text", "content": data.text}

