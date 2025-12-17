#!/usr/bin/env pwsh
Set-StrictMode -Version Latest

Write-Host "=== Multimodal Analyzer - Full Setup ===" -ForegroundColor Green
Write-Host ""

# Create and activate venv
Write-Host "1. Setting up Python virtual environment..." -ForegroundColor Cyan
python -m venv venv
& .\venv\Scripts\Activate.ps1

# Install backend dependencies
Write-Host "2. Installing backend dependencies..." -ForegroundColor Cyan
pip install --upgrade pip
pip install -r requirements.txt

# Download spacy model
Write-Host "3. Downloading spacy model..." -ForegroundColor Cyan
python -m spacy download en_core_web_sm

# Install frontend dependencies
Write-Host "4. Installing frontend dependencies..." -ForegroundColor Cyan
Push-Location frontend
npm install
Write-Host "5. Building frontend..." -ForegroundColor Cyan
npm run build
Pop-Location

# Create .env if not exists
if (-not (Test-Path .env)) {
  Write-Host "6. Creating .env file..." -ForegroundColor Cyan
  @"
OPENAI_API_KEY=your_key_here
"@ | Out-File -Encoding UTF8 .env
  Write-Host "   ??  Update .env with your OPENAI_API_KEY" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== Setup Complete ===" -ForegroundColor Green
Write-Host ""
Write-Host "To start the application:" -ForegroundColor Cyan
Write-Host "  .\venv\Scripts\Activate.ps1"
Write-Host "  python backend/app.py"
Write-Host ""
Write-Host "Then open: http://localhost:8000" -ForegroundColor Green
