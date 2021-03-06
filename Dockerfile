FROM python:3

ENV PYTHONUNBUFFERED=1


COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt



WORKDIR /app
ADD . .

EXPOSE 8000

CMD ["gunicorn", "--bind",":8000", "--workers", "3", "core.wsgi:application"] 