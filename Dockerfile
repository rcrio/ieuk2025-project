FROM python:3.11-slim
WORKDIR /app

# Copy all files except requirements.txt first
COPY . .

# Install dependencies only if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

CMD ["python", "main.py"]