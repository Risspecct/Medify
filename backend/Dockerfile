# backend.Dockerfile
FROM python:3.11-slim

WORKDIR /code

# Install system deps (only if needed for Pandas/Watson ML etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl \
    && rm -rf /var/lib/apt/lists/*

# Install backend dependencies (cached layer)
COPY backend_requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy only backend source
COPY backend ./backend
COPY datasets/dosage.csv ./datasets/dosage.csv

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
