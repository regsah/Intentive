from transformers import pipeline

emotions = [
    "neşe",
    "öfke",
    "üzüntü",
    "korku",
    "şaşkınlık",
    "iğrenme",  
    "nötr"
]


classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_emotion(text: str) -> str:
    result = classifier(text, candidate_labels=emotions, multi_label=False)
    return result['labels'][0]
