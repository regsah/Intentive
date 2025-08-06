import sqlite3
import os

from app.utils.paths import LOCAL_STORAGE_DIR
DB_PATH = os.path.join(LOCAL_STORAGE_DIR, "text_submissions.db")

def get_label_id(cursor: sqlite3.Cursor, table: str, label: str) -> int:
    cursor.execute(f"SELECT id FROM {table} WHERE label = ?", (label,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        raise ValueError(f"Label '{label}' not found in table '{table}'")


def add_entry(entry: dict) -> None:
    entry_id = entry['id']
    input_type = entry['type']
    query = entry['content']
    intent = entry['intent']
    emotion = entry['emotion']
    try:
            
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("INSERT OR IGNORE INTO intent (label) VALUES (?)", (intent,))
            intent_id = get_label_id(cursor, "intent", intent)

            cursor.execute("INSERT OR IGNORE INTO emotion (label) VALUES (?)", (emotion,))
            emotion_id = get_label_id(cursor, "emotion", emotion)

            cursor.execute("INSERT OR IGNORE INTO input_type (label) VALUES (?)", (input_type,))
            type_id = get_label_id(cursor, "input_type", input_type)

            cursor.execute(
                """
                INSERT INTO entry (id, query, intent_id, emotion_id, type_id)
                VALUES (?, ?, ?, ?, ?)
                """,
                (entry_id, query, intent_id, emotion_id, type_id)
            )
            conn.commit()
    except sqlite3.IntegrityError as e:
        raise sqlite3.IntegrityError(f"Entry with id '{entry_id}' already exists.") from e

def get_entries(intent_label: str = None, emotion_label: str = None, type_label: str = None) -> list[dict]:
    query = """
        SELECT e.id, e.query, i.label AS intent, em.label AS emotion, it.label AS type
        FROM entry e
        JOIN intent i ON e.intent_id = i.id
        JOIN emotion em ON e.emotion_id = em.id
        JOIN input_type it ON e.type_id = it.id
        where 1=1
    """

    params = []

    if intent_label:
        query += " AND i.label = ?"
        params.append(intent_label)
    if emotion_label:
        query += " AND em.label = ?"
        params.append(emotion_label)
    if type_label:
        query += " AND it.label = ?"
        params.append(type_label)
    
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
    
    results = [
        {
            "id": row[0],
            "query": row[1],
            "intent": row[2],
            "emotion": row[3],
            "type": row[4]
        } for row in rows
    ]
    return results

def get_labels(table: str) -> list[str]:
    valid_tables = {"intent", "emotion", "input_type"}
    if table not in valid_tables:
        raise ValueError(f"Invalid table '{table}'. Must be one of {valid_tables}.")

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT label FROM {table}")
        rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_intents() -> list[str]:
    return get_labels("intent")

def get_emotions() -> list[str]:
    return get_labels("emotion")

def get_input_types() -> list[str]:
    return get_labels("input_type")

def delete_by_id(entry_id: str) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("DELETE FROM entry WHERE id = ?", (entry_id,))
        conn.commit()