# syntax=docker/dockerfile:1

FROM alpine

WORKDIR /python-docker

RUN apk add --no-cache python3 py3-pip
RUN apk add py3-flask


COPY . .

CMD ["python3", "app.py"]