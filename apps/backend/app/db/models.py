# FASTAPI

from pydantic import BaseModel
from uuid import UUID

class TextInput(BaseModel):
    id: UUID
    text: str


# ------------------------------------------------
# SQLAlchemy

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Intent(Base):
    __tablename__ = "intent"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, unique=True, nullable=False)

    entries = relationship("Entry", back_populates="intent")


class Emotion(Base):
    __tablename__ = "emotion"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, unique=True, nullable=False)

    entries = relationship("Entry", back_populates="emotion")


class InputType(Base):
    __tablename__ = "input_type"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, unique=True, nullable=False)

    entries = relationship("Entry", back_populates="input_type")


class Entry(Base):
    __tablename__ = "entry"

    id = Column(String, primary_key=True, index=True)  # UUID
    query = Column(String, nullable=False)

    intent_id = Column(Integer, ForeignKey("intent.id"), nullable=False)
    emotion_id = Column(Integer, ForeignKey("emotion.id"), nullable=False)
    input_type_id = Column(Integer, ForeignKey("input_type.id"), nullable=False)

    intent = relationship("Intent", back_populates="entries")
    emotion = relationship("Emotion", back_populates="entries")
    input_type = relationship("InputType", back_populates="entries")
