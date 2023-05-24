FROM python:3.10-slim

WORKDIR /app

COPY ./ /app

RUN pip3 install -r requirements.txt --no-cache-dir

CMD python project/manage.py runserver 0.0.0.0:8000
