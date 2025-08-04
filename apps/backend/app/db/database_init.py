import sqlite3
import os

from app.utils.paths import LOCAL_STORAGE_DIR

# Path to the SQLite database file (located in local_storage/)
DB_PATH = os.path.join(LOCAL_STORAGE_DIR, "text_submissions.db")

def create_tables():
    os.makedirs(LOCAL_STORAGE_DIR, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS intent (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    label TEXT UNIQUE NOT NULL
                );
            """
        )

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS emotion (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    label TEXT UNIQUE NOT NULL
                );
            """
        )

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS input_type (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    label TEXT UNIQUE NOT NULL
                );
            """
        )

        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS entry (
                id TEXT PRIMARY KEY, -- Use UUID
                query TEXT NOT NULL,
                intent_id INTEGER,
                emotion_id INTEGER,
                type_id INTEGER,
                FOREIGN KEY (intent_id) REFERENCES intent(id),
                FOREIGN KEY (emotion_id) REFERENCES emotion(id),
                FOREIGN KEY (type_id) REFERENCES input_type(id)
            );
        """
        )

        conn.commit()
    print("Tables created successfully.")

def seed_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        intents = ["account services", "money transfer and payments", "card services", 
                   "loans", "investment and advisory", "customer service"]
        for intent in intents:
            cursor.execute("INSERT OR IGNORE INTO intent (label) VALUES (?);", (intent,))

        emotions = ["joy", "anger", "sadness", "fear", "surprise", "disgust", "neutral"]
        for emotion in emotions:
            cursor.execute("INSERT OR IGNORE INTO emotion (label) VALUES (?);", (emotion,))

        input_types = ["text", "audio"]
        for input_type in input_types:
            cursor.execute("INSERT OR IGNORE INTO input_type (label) VALUES (?);", (input_type,))

        conn.commit()
    print("Tables seeded successfully.")

if __name__ == "__main__":
    create_tables()
    seed_tables()
