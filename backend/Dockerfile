# Use a lightweight Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files & keep stdout unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory directly to the backend folder
WORKDIR /app/backend

# Install system dependencies required for ML packages (gcc, g++, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements FIRST to leverage Docker layer caching
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend source code (this automatically includes backend/datasets/)
COPY backend/ .

# Set Environment Variables pointing to the correct datasets path inside the container
ENV DOSAGE_FILE_PATH=/app/backend/datasets/dosage.csv

EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]# Use a lightweight Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files & keep stdout unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory directly to the backend folder
WORKDIR /app/backend

# Install system dependencies required for ML packages (gcc, g++, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements FIRST to leverage Docker layer caching
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend source code (this automatically includes backend/datasets/)
COPY backend/ .

# Set Environment Variables pointing to the correct datasets path inside the container
ENV DOSAGE_FILE_PATH=/app/backend/datasets/dosage.csv

EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]