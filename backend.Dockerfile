# backend.Dockerfile
FROM python:3.11-slim
WORKDIR /code

# Install dependencies
COPY backend_requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary backend folders and files
COPY ./backend ./backend
COPY ./datasets/dosage.csv ./datasets/dosage.csv