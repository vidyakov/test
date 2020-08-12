FROM python:3.8

RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /srv/www/test_webim
COPY ./requirements.txt /srv/www/test_webim
RUN pip install -r requirements.txt


COPY ./project /srv/www/test_webim
RUN python manage.py collectstatic --noinput
