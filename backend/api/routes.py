"""
Flask routes for multimodal analyzer (MVP).
"""
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
import uuid
import tempfile
from ..services.content_analyzer import ContentAnalyzer

bp = Blueprint("api", __name__)
ANALYZER = ContentAnalyzer(llm_api_key=os.getenv("OPENAI_API_KEY"))


@bp.route("/analyze/image", methods=["POST"])
def analyze_image():
    if "file" not in request.files:
        return jsonify({"error": "file required"}), 400
    f = request.files["file"]
    filename = secure_filename(f.filename)
    temp_dir = tempfile.gettempdir()
    tmp = os.path.join(temp_dir, f"{uuid.uuid4().hex}_{filename}")
    f.save(tmp)
    res = ANALYZER.analyze(image_path=tmp)
    return jsonify(res)


@bp.route("/analyze/text", methods=["POST"])
def analyze_text():
    data = request.get_json() or {}
    text = data.get("text")
    if not text:
        return jsonify({"error": "text required"}), 400
    res = ANALYZER.analyze(text=text)
    return jsonify(res)


@bp.route("/analyze/multimodal", methods=["POST"])
def analyze_multimodal():
    text = request.form.get("text")
    file = request.files.get("file")
    tmp = None
    if file:
        filename = secure_filename(file.filename)
        temp_dir = tempfile.gettempdir()
        tmp = os.path.join(temp_dir, f"{uuid.uuid4().hex}_{filename}")
        file.save(tmp)
    res = ANALYZER.analyze(image_path=tmp, text=text)
    return jsonify(res)