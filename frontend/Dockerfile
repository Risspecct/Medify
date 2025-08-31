# frontend.Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system deps (needed for torch/transformers/vision libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libglib2.0-0 libsm6 libxrender1 libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install frontend dependencies first (cached)
COPY frontend_requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend code
COPY app.py .
COPY features ./features
COPY datasets/alt_dataset.py ./datasets/alt_dataset.py
COPY datasets/ner_dataset.py ./datasets/ner_dataset.py

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
