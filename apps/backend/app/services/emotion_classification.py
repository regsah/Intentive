from transformers import pipeline

from app.db.database_scripts import get_emotions
from app.api.helper import safe_fetch

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

async def classify_emotion(text: str) -> str:
    labels = await safe_fetch(get_emotions)
    result = classifier(text, candidate_labels=labels["data"], multi_label=False)
    return result['labels'][0]
