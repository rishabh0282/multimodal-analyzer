"""
NLPAnalyzer (MVP): sentiment, NER (spacy), basic stats.
"""
from typing import Dict, Any
import logging
from transformers import pipeline
import spacy

logger = logging.getLogger(__name__)


class NLPAnalyzer:
    def __init__(self):
        self.sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except Exception:
            self.nlp = None

    def analyze(self, text: str) -> Dict[str, Any]:
        try:
            sent = self.sentiment(text[:1000])
            ents = []
            if self.nlp:
                doc = self.nlp(text)
                ents = [{"text": e.text, "label": e.label_} for e in doc.ents]
            stats = {"word_count": len(text.split()), "char_count": len(text)}
            return {"sentiment": sent, "entities": ents, "stats": stats}
        except Exception:
            logger.exception("NLP analysis failed")
            raise