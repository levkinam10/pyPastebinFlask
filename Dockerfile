# syntax=docker/dockerfile:1

FROM alpine

WORKDIR /python-docker

RUN apk add --no-cache python3 py3-pip py3-flask

EXPOSE 80

COPY . .

CMD ["python3", "app.py"]