# Light-weight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY api_requirements.txt .

# Set Labels
LABEL org.opencontainers.image.title="Burrow Wheeler Transform API App"
LABEL org.opencontainers.image.description="FastAPI App to elaborate strings using the Burrow Wheeler algorithm."
LABEL org.opencontainers.image.version="1.0.0"

# Install Python dependencies
RUN pip install --no-cache-dir -r api_requirements.txt

# Copy app code
COPY api.py .
COPY ./Components/ ./Components/

# Expose port 8000 
EXPOSE 8000

# Start app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]