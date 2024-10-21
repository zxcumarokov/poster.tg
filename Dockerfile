FROM python:3.12.6-slim-bookworm

RUN apt update
RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app
