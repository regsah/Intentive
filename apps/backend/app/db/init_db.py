import asyncio
from app.db.database import engine, Base, AsyncSessionLocal
from app.db.models import Intent, Emotion, InputType
from sqlalchemy import select

intents = [
    "account services",
    "money transfer and payments",
    "card services",
    "loans",
    "investment and advisory",
    "customer service",
]

emotions = [
    "joy",
    "anger",
    "sadness",
    "fear",
    "surprise",
    "disgust",
    "neutral",
]

input_types = [
    "text",
    "audio",
]

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully.")

async def seed_tables():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Intent.label))
        existing_intent_labels = {label for (label,) in result.all()}
        new_intents = [label for label in intents if label not in existing_intent_labels]
        session.add_all([Intent(label=label) for label in new_intents])

        result = await session.execute(select(Emotion.label))
        existing_emotion_labels = {label for (label,) in result.all()}
        new_emotions = [label for label in emotions if label not in existing_emotion_labels]
        session.add_all([Emotion(label=label) for label in new_emotions])

        result = await session.execute(select(InputType.label))
        existing_input_type_labels = {label for (label,) in result.all()}
        new_input_types = [label for label in input_types if label not in existing_input_type_labels]
        session.add_all([InputType(label=label) for label in new_input_types])

        await session.commit()
    print("Tables seeded successfully.")

async def main():
    await create_tables()
    await seed_tables()

if __name__ == "__main__":
    asyncio.run(main())
