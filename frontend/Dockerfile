# Use a lightweight Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files & keep stdout unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory directly to the frontend folder
WORKDIR /app/frontend

# Copy requirements first to leverage Docker layer caching
COPY frontend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend source code
COPY frontend/ .

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]