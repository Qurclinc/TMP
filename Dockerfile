FROM python:3.12-slim

WORKDIR /app

RUN pip3 install flask

COPY . .

CMD ["python3", "main.py"]
