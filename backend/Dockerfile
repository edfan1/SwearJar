# Use an official Python runtime as the base image
FROM python:3.12-bullseye

# Copy only the requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
