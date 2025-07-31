from pydantic import BaseModel
from uuid import UUID

class TextInput(BaseModel):
    id: UUID
    text: str
