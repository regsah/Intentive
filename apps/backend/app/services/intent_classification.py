from transformers import pipeline

from app.db.database_scripts import get_intents

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_intent(text: str) -> str:
    result = classifier(text, candidate_labels=get_intents(), multi_label=False)
    return result['labels'][0]