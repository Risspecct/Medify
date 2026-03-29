# Use a slim Python image to keep the size small
FROM python:3.11-slim

# Set the working directory for all subsequent commands
WORKDIR /app

# Install system-level dependencies required for building some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker layer caching
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend source code and datasets into the container
COPY backend/ . 
COPY datasets ./datasets

# Set environment variables for the application
ENV DOSAGE_FILE_PATH=/app/datasets/dosage.csv
EXPOSE 8000

# Start the FastAPI server using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]