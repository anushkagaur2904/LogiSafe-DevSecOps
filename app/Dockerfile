# Use lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose Flask port
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]
