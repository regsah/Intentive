from typing import List, Optional
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Intent, Emotion, InputType, Entry


async def get_label_id(session: AsyncSession, model, label: str) -> int:
    orm_query = select(model).where(model.label == label)
    result = await session.execute(orm_query)
    obj = result.scalar_one_or_none()
    
    if obj: return obj.id
    raise ValueError(f"Label '{label}' not found in {model.__tablename__}")


async def get_labels(session: AsyncSession, model) -> list[str]:
    result = await session.execute(select(model))
    labels = [obj.label for obj in result.scalars().all()]
    return labels

async def get_intents(session: AsyncSession) -> list[str]:
    return await get_labels(session, Intent)

async def get_emotions(session: AsyncSession) -> list[str]:
    return await get_labels(session, Emotion)

async def get_input_types(session: AsyncSession) -> list[str]:
    return await get_labels(session, InputType)

async def get_or_create_label(session: AsyncSession, model, label: str) -> int:
    try:
        return await get_label_id(session, model, label)
    except ValueError:
        obj = model(label=label)
        session.add(obj)
        await session.flush()
        return obj.id


async def add_entry(session: AsyncSession, entry: dict) -> None:
    entry_id = entry['id']
    query = entry['content']
    intent = entry['intent']
    emotion = entry['emotion']
    input_type = entry['type']

    intent_id = await get_or_create_label(session, Intent, intent)
    emotion_id = await get_or_create_label(session, Emotion, emotion)
    input_type_id = await get_or_create_label(session, InputType, input_type)

    new_entry = Entry(
        id=entry_id,
        query=query,
        intent_id=intent_id,
        emotion_id=emotion_id,
        input_type_id=input_type_id
    )
    session.add(new_entry)
    try:
        await session.flush()
    except IntegrityError as e:
        raise IntegrityError(f"Entry with id '{entry_id}' already exists.") from e
        


async def get_entries(session: AsyncSession, intent_label: str = None, 
                emotion_label: str = None, input_type_label: str = None) -> list[dict]:
    
    query = select(Entry).options(
        selectinload(Entry.intent),
        selectinload(Entry.emotion),
        selectinload(Entry.input_type)
    )

    if intent_label:
        query = query.join(Entry.intent).where(Intent.label == intent_label)
    if emotion_label:
        query = query.join(Entry.emotion).where(Emotion.label == emotion_label)
    if input_type_label:
        query = query.join(Entry.input_type).where(InputType.label == input_type_label)

    result = await session.execute(query)
    entries = result.scalars().all()

    return [
        {
            "id": entry.id,
            "query": entry.query,
            "intent": entry.intent.label,
            "emotion": entry.emotion.label,
            "type": entry.input_type.label,
        }
        for entry in entries
    ]

async def delete_by_id(session: AsyncSession, model, elem_id: str) -> None:
    result = await session.execute(delete(model).where(model.id == elem_id))
    if result.rowcount == 0:
        raise ValueError(f"No entry found with id '{elem_id}'")