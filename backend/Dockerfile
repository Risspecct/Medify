FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend source code into the /app directory
COPY backend/ .

# Copy the datasets into the /app directory
COPY datasets ./datasets

# Set the absolute path for the dosage file inside the container
ENV DOSAGE_FILE_PATH=/app/datasets/dosage.csv

EXPOSE 8000

# The command now runs from /app, so it can find main.py directly
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
