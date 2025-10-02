# content_preprocess.py
import re
import nltk
from nltk.tokenize import sent_tokenize

# Download NLTK resources (run once)
nltk.download("punkt")

def clean_text(text: str) -> str:
    """
    Clean raw text:
    - Remove URLs
    - Remove extra spaces and newlines
    - Remove non-alphanumeric characters except basic punctuation
    """
    text = re.sub(r"http\S+|www\S+", "", text)  # remove URLs
    text = re.sub(r"\s+", " ", text)  # collapse multiple spaces/newlines
    text = re.sub(r"[^a-zA-Z0-9.,!?;:() ]", "", text)  # remove special chars
    return text.strip()

def extract_relevant_sentences(text: str, min_len: int = 30) -> list:
    """
    Split text into sentences and keep sentences longer than min_len characters.
    Minimal preprocessing to preserve sentence structure.
    """
    text = clean_text(text)
    sentences = sent_tokenize(text)
    relevant = [sent.strip() for sent in sentences if len(sent.strip()) >= min_len]
    return relevant
