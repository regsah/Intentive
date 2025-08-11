import pytest
import asyncio
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.db.models import Base, Intent, Emotion, InputType, Entry
from app.db import database_scripts as scripts

# ----------------
# FIXTURES
# ----------------

@pytest.fixture(scope="session")
def event_loop():
    """Required for pytest-asyncio with session scope."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture
async def async_engine():
    # Use in-memory SQLite
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()

@pytest_asyncio.fixture
async def session(async_engine):
    """Creates a fresh session with rollback after each test."""
    async_session = sessionmaker(
        bind=async_engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        yield session
        await session.rollback()

# ----------------
# TESTS
# ----------------

@pytest.mark.asyncio
async def test_get_or_create_label_creates_and_returns_id(session):
    intent_id = await scripts.get_or_create_label(session, Intent, "greeting")
    assert isinstance(intent_id, int)

    same_id = await scripts.get_or_create_label(session, Intent, "greeting")
    assert intent_id == same_id

@pytest.mark.asyncio
async def test_add_and_get_entries(session):
    entry_data = {
        "id": "123",
        "content": "Hello there!",
        "intent": "greeting",
        "emotion": "happy",
        "type": "text"
    }

    await scripts.add_entry(session, entry_data)

    results = await scripts.get_entries(session)
    assert len(results) == 1
    assert results[0]["query"] == "Hello there!"
    assert results[0]["intent"] == "greeting"
    assert results[0]["emotion"] == "happy"
    assert results[0]["type"] == "text"

@pytest.mark.asyncio
async def test_get_entries_with_filters(session):
    await scripts.add_entry(session, {
        "id": "1",
        "content": "Hi",
        "intent": "greeting",
        "emotion": "happy",
        "type": "text"
    })
    await scripts.add_entry(session, {
        "id": "2",
        "content": "Bye",
        "intent": "farewell",
        "emotion": "sad",
        "type": "text"
    })

    filtered = await scripts.get_entries(session, intent_label="farewell")
    assert len(filtered) == 1
    assert filtered[0]["intent"] == "farewell"

@pytest.mark.asyncio
async def test_delete_by_id(session):
    intent_id = await scripts.get_or_create_label(session, Intent, "test")
    await scripts.delete_by_id(session, Intent, intent_id)

    with pytest.raises(ValueError):
        await scripts.delete_by_id(session, Intent, intent_id)