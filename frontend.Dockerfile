# frontend.Dockerfile
FROM python:3.11-slim
WORKDIR /app

# Install dependencies
COPY frontend_requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary frontend folders and files
COPY app.py .
COPY ./features ./features
COPY ./datasets/alt_dataset.py ./datasets/alt_dataset.py
COPY ./datasets/ner_dataset.py ./datasets/ner_dataset.py