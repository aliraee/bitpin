FROM python:3.10

RUN pip3 install --upgrade pip

ENV PYTHONBUFFERED 1

WORKDIR /code

COPY req.txt /code/
RUN pip3 install -r req.txt

COPY ./interview_task/ /code/
