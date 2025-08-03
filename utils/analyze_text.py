
import re
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

filler_words = ["um", "uh", "like", "you know", "so", "actually"]

def count_fillers(text):
    return sum(text.lower().split().count(word) for word in filler_words)

def avg_sentence_length(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    words = text.split()
    return round(len(words) / len(sentences), 2) if sentences else 0

def grammar_score(text):
    tokenizer = AutoTokenizer.from_pretrained("textattack/roberta-base-CoLA")
    model = AutoModelForSequenceClassification.from_pretrained("textattack/roberta-base-CoLA")
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    score = torch.softmax(outputs.logits, dim=1)[0][1].item()
    return round(score * 100, 1)
