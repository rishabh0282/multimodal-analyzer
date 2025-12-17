#!/usr/bin/env bash
set -euo pipefail
python -m venv venv
if [ -f "venv/bin/activate" ]; then
  source venv/bin/activate
fi
pip install --upgrade pip
pip install -r requirements.txt
echo "Multimodal analyzer setup complete."