# syntax = docker/dockerfile:1.0-experimental
FROM python:3.9.2-buster

# The steps should be ordered from less frequently changed to most
# To be able to split the cacheable layers and decrease build time

ENV ENV PYTHONUNBUFFERED=1

RUN set -xe \
  && apt-get update -q \
  && apt-get install -y -q gcc \
  && python3 -m pip install --upgrade pip poetry==1.1.5;


# Project initialization:
WORKDIR /
COPY poetry.lock pyproject.toml /

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

COPY . /