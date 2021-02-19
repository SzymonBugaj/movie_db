FROM python:3.8
ENV PYTHONUNBUFFERED 1

COPY requirements_dev.txt /requirements_dev.txt
COPY requirements.txt /requirements.txt

RUN apt-get update && apt-get install
RUN pip install -r /requirements_dev.txt

