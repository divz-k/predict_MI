# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY deploy_model.py .
COPY best_logistic_regression_model.pkl .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "deploy_model:app", "--host", "0.0.0.0", "--port", "8000"]
