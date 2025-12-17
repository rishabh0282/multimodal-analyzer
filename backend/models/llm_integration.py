"""
LLM integration (MVP) using OpenAI: summary generation stub with retries.
"""
import os
import openai
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class LLMIntegrator:
    def __init__(self, api_key: str = None):
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        self.api_key = os.getenv("OPENAI_API_KEY")

    def generate_summary(self, multimodal_results: Dict[str, Any]) -> str:
        # Minimal safe wrapper: return a constructed summary. Replace call with OpenAI if key present.
        if not self.api_key:
            # fallback simple summary
            return f"Summary: {multimodal_results.get('summary_stub', 'No API key. Provide OPENAI_API_KEY to enable full summaries.')}"
        try:
            openai.api_key = self.api_key
            prompt = "Summarize the following multimodal results:\n\n" + str(multimodal_results)
            resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}], max_tokens=300)
            return resp.choices[0].message.content
        except Exception:
            logger.exception("LLM call failed")
            raise