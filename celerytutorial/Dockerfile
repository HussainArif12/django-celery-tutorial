FROM python:3.12-alpine
WORKDIR /app
COPY . .
RUN pip install djangorestframework redis celery  psycopg[binary] django-celery-results