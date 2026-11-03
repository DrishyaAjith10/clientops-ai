
# 1. Base Python image
FROM python:3.12-slim

# 2. Prevent Python from generating bytecode
ENV PYTHONDONTWRITEBYTECODE=1

# 3. Display logs immediately
ENV PYTHONUNBUFFERED=1

# 4. Set working directory inside container
WORKDIR /app

# 5. Copy dependency list
COPY requirements_docker.txt .

# 6. Install dependencies
RUN pip install --no-cache-dir -r requirements_docker.txt

# 7. Copy application code
COPY . .

# 8. Expose FastAPI port
EXPOSE 8000

# 9. Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
