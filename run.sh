#!/bin/bash
# Simple script to set up environment and run Flask app

# Stop script if any command fails
set -e

# Activate virtual environment if present
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "⚠️  No virtual environment found. Run 'python3 -m venv venv' first."
fi

# Install dependencies
pip install -r requirements.txt

# Set Flask app environment variable
export FLASK_APP=app.py
export FLASK_ENV=development   # enables debug mode

# Run Flask
flask run

