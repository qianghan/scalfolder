FROM python:3.10-slim

# Install system deps (if needed)
# RUN apt-get update && apt-get install -y ...

# Create a working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
# This will install both the main project and the dev deps
RUN pip install --upgrade pip && pip install -e .[dev]

# Expose ComfyUI's default port (if you run it inside Docker)
EXPOSE 8188

# Optionally, you can run ComfyUI as an entrypoint
# but that depends on how you structure your environment
# ENTRYPOINT ["python", "run.py"]
