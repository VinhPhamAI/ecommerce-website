# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and clean up
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Ensure the entrypoint script is executable (Python doesn't need this but to match .sh file habit)
RUN chmod +x /app/entrypoint.py

# Expose the port that the app runs on
EXPOSE 8000

# Use the Python script as the entrypoint to run migrations, create superuser, and import CSV data
ENTRYPOINT ["python", "/app/entrypoint.py"]
