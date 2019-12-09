FROM python:alpine3.7
LABEL version 1.0

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app  

RUN adduser -D recipe_user
USER recipe_user