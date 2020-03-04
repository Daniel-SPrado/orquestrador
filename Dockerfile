FROM python:3

WORKDIR /usr/src/app
COPY setup.py orquestrador/execute/app.py

RUN pip install -e .

COPY . .
