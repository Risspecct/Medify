FROM python:3.11-slim

WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl \
    && rm -rf /var/lib/apt/lists/*

# Install backend dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source + only dosage.csv
COPY backend ./backend
COPY datasets ./datasets

# Set env var so code always knows where to look
ENV DOSAGE_FILE_PATH=/code/datasets/dosage.csv

EXPOSE 8000

# Use Gunicorn Uvicorn for production
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
