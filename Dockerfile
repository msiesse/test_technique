FROM python:3.10-slim-buster

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]