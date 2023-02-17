FROM python:3.10-slim-buster

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get upgrade -y
RUN apt-get install gcc libpq-dev python3-dev -y

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]