FROM python:3.6-alpine
MAINTAINER Lucas Rocha

COPY ./requirements.txt /requirements.txt
COPY ./run_api.sh /run_api.sh

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -r requirements.txt

RUN mkdir /luizalabs
WORKDIR /luizalabs
COPY ./luizalabs /luizalabs

RUN adduser -D user
USER user
