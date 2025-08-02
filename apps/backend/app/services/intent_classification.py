from transformers import pipeline

intents = [
    "hesap bakiyesi sorgulama",
    "para transferi",
    "fatura ödeme",
    "yeni hesap açma",
    "hesap kapatma",
    "kayıp veya çalıntı kart bildirimi",
    "dolandırıcılık bildirimi",
    "kredi başvurusu",
    "kredi kartı başvurusu",
    "kişisel bilgileri güncelleme",
    "şube bulucu",
    "ATM bulucu",
    "PIN değiştirme",
    "şifre sıfırlama",
    "yatırım tavsiyesi",
    "hesap ekstresi talebi",
    "işlem itirazı",
    "faiz oranları sorgulama",
    "konut kredisi bilgisi",
    "müşteri hizmetleri",
]

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_intent(text: str) -> str:
    result = classifier(text, candidate_labels=intents, multi_label=False)
    return result['labels'][0]