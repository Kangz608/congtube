FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code/
RUN mkdir /code/congtube/

ADD ./congtube/ /code/congtube/
ADD ./requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt 

WORKDIR /code/congtube/

ENV DJANGO_CONFIGURATION Production
ENV DJANGO_SETTINGS_MODULE config.settings

RUN python3 manage.py collectstatic -v2 --noinput
