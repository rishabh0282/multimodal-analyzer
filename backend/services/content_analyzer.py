"""
Orchestrator combining vision and NLP and LLM summary.
"""
from typing import Dict, Any, Optional
import logging

from ..models.vision_model import VisionAnalyzer
from ..models.nlp_model import NLPAnalyzer
from ..models.llm_integration import LLMIntegrator

logger = logging.getLogger(__name__)


class ContentAnalyzer:
    def __init__(self, llm_api_key: Optional[str] = None):
        self.vision = VisionAnalyzer()
        self.nlp = NLPAnalyzer()
        self.llm = LLMIntegrator(api_key=llm_api_key)

    def analyze(self, image_path: str = None, text: str = None) -> Dict[str, Any]:
        results = {}
        if image_path:
            results["vision"] = self.vision.analyze(image_path)
        if text:
            results["nlp"] = self.nlp.analyze(text)
        results["summary_stub"] = "Use LLM to synthesize vision + text results."
        results["summary"] = self.llm.generate_summary(results)
        return results