#!/usr/bin/env bash
set -euo pipefail

echo "=== Multimodal Analyzer - Full Setup ==="
echo ""

# Create and activate venv
echo "1. Setting up Python virtual environment..."
python -m venv venv
source venv/bin/activate

# Install backend dependencies
echo "2. Installing backend dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Download spacy model
echo "3. Downloading spacy model..."
python -m spacy download en_core_web_sm

# Install frontend dependencies
echo "4. Installing frontend dependencies..."
cd frontend
npm install
echo "5. Building frontend..."
npm run build
cd ..

# Create .env if not exists
if [ ! -f .env ]; then
  echo "6. Creating .env file..."
  cat > .env << 'EOF'
OPENAI_API_KEY=your_key_here
EOF
  echo "   ??  Update .env with your OPENAI_API_KEY"
fi

echo ""
echo "=== Setup Complete ==="
echo ""
echo "To start the application:"
echo "  source venv/bin/activate"
echo "  python backend/app.py"
echo ""
echo "Then open: http://localhost:8000"
