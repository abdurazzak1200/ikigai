FROM python:3.8.6-alpine3.12
LABEL maintainer="Abi"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek

RUN apk add --no-cache gcc postgresql-dev zlib-dev \
    libjpeg-turbo-dev gettext linux-headers musl-dev make \
    python3-dev libffi-dev openssl-dev cargo  postgresql-client \
    && rm -rf /var/apt/list/*

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "./dockerfiles/docker-entrypoint.sh"]
