from transformers import pipeline

from app.db.database_scripts import get_emotions

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_emotion(text: str) -> str:
    result = classifier(text, candidate_labels=get_emotions(), multi_label=False)
    return result['labels'][0]
