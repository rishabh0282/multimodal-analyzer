"""
VisionAnalyzer (MVP): feature extraction and caption stub.
"""
from typing import Dict, Any
from PIL import Image
import torch
from torchvision import models, transforms
import logging

logger = logging.getLogger(__name__)


class VisionAnalyzer:
    def __init__(self, device: str = "cpu"):
        self.device = device
        self.model = models.resnet50(pretrained=True).eval().to(device)
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def analyze(self, image_path: str) -> Dict[str, Any]:
        try:
            img = Image.open(image_path).convert("RGB")
            input_t = self.preprocess(img).unsqueeze(0).to(self.device)
            with torch.no_grad():
                feats = self.model.fc(input_t).cpu().numpy().tolist()
            # caption generation omitted (stub)
            return {"features": feats, "caption": "caption-stub", "format": img.format}
        except Exception:
            logger.exception("Vision analysis failed for %s", image_path)
            raise