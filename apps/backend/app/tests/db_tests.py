import sys
import os

from app.db.database_scripts import get_emotions, get_intents, get_input_types

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

if __name__ == "__main__":
    test_get_emotions()
    test_get_intents()
    test_get_input_types()
    print("All tests passed!")
    sys.exit(0)