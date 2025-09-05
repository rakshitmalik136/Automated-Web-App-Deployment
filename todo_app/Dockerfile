# Base Image
FROM python:3.11-slim

# Work Directory
WORKDIR /app

# Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Files
COPY . .

# Expose Port
EXPOSE 5000

# Environment Variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run App
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
