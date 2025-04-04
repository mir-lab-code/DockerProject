FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY static/upload.html static/upload.html

EXPOSE 8000

CMD ["python", "app.py"]