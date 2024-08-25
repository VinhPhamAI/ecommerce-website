# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev && apt-get clean

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8000

# Ensure the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Use the entrypoint script to run migrations, create superuser, and import CSV data
ENTRYPOINT ["/app/entrypoint.sh"]
