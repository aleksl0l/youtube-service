FROM python:3.6-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev bash

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .