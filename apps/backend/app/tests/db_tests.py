import sys
import os

from app.db.database_scripts import *

def test_get_emotions():
    print("Testing get_emotions()")
    emotions = get_emotions()
    print("Emotions:", emotions)
    assert isinstance(emotions, list)
    assert len(emotions) > 0
    assert all(isinstance(emotion, str) for emotion in emotions)

def test_get_intents():
    print("Testing get_intents()")
    intents = get_intents()
    print("Intents:", intents)
    assert isinstance(intents, list)
    assert len(intents) > 0
    assert all(isinstance(intent, str) for intent in intents)

def test_get_input_types():
    print("Testing get_input_types()")
    input_types = get_input_types()
    print("Input Types:", input_types)
    assert isinstance(input_types, list)
    assert len(input_types) > 0
    assert all(isinstance(input_type, str) for input_type in input_types)

def test_get_entries():
    print("Testing get_entries with no filters")
    entries = get_entries()
    print(f"Total entries found: {len(entries)}")
    assert isinstance(entries, list)

    if not entries:
        print("No entries found. Consider inserting test data before running this test.")
        return

    first_entry = entries[0]
    print("Sample entry:", first_entry)

    # Test filter by intent_label
    intent_label = first_entry['intent']
    filtered_intent = get_entries(intent_label=intent_label)
    print(f"Entries filtered by intent='{intent_label}': {len(filtered_intent)}")
    assert all(e['intent'] == intent_label for e in filtered_intent)

    # Test filter by emotion_label
    emotion_label = first_entry['emotion']
    filtered_emotion = get_entries(emotion_label=emotion_label)
    print(f"Entries filtered by emotion='{emotion_label}': {len(filtered_emotion)}")
    assert all(e['emotion'] == emotion_label for e in filtered_emotion)

    # Test filter by type_label
    type_label = first_entry['type']
    filtered_type = get_entries(type_label=type_label)
    print(f"Entries filtered by type='{type_label}': {len(filtered_type)}")
    assert all(e['type'] == type_label for e in filtered_type)

    # Test combined filters
    filtered_combined = get_entries(intent_label=intent_label, emotion_label=emotion_label, type_label=type_label)
    print(f"Entries filtered by intent='{intent_label}', emotion='{emotion_label}', type='{type_label}': {len(filtered_combined)}")
    for e in filtered_combined:
        assert e['intent'] == intent_label and e['emotion'] == emotion_label and e['type'] == type_label

    print("get_entries tests passed.")

if __name__ == "__main__":
    test_get_emotions()
    test_get_intents()
    test_get_input_types()
    test_get_entries()
    print("All database tests passed!")
    sys.exit(0)