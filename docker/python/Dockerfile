FROM python:3.8.3

WORKDIR /srv/www/test_webim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /srv/www/test_webim
RUN pip install -r requirements.txt


COPY ./project /srv/www/test_webim