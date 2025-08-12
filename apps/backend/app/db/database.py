import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import event
from app.utils.paths import LOCAL_STORAGE_DIR

DB_PATH = os.path.join(LOCAL_STORAGE_DIR, "submissions.db")
DATABASE_URL = f"sqlite+aiosqlite:///{DB_PATH}"

# Base for db models
Base = declarative_base()


# connections
engine = create_async_engine(
    DATABASE_URL,
    echo=True, # just for development
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# for foreign key safety
@event.listens_for(engine.sync_engine, "connect")
def enable_sqlite_fk(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# for routes  
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
