# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1

# Install OpenLLM from PyPI
RUN pip install openllm[llama]

# Expose the port the OpenLLM server will run on
EXPOSE 3000

# Set the command to start the OpenLLM server
CMD ["openllm", "start", "llama", "--model-id", "meta-llama/Llama-2-70b-chat-hf"]
