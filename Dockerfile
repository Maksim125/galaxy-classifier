FROM python:3.10.11-slim as final

RUN \
    apt install -qq && \
    apt-get update -qq && \
    apt-get install -y linux-headers-generic libgl1 && \
    apt-get install -yq --no-install-recommends libgtk2.0-dev

RUN \
    pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade poetry

WORKDIR /galaxy-classifier

COPY app /galaxy-classifier/app

COPY poetry.lock /galaxy-classifier
COPY pyproject.toml /galaxy-classifier

RUN \
    poetry config virtualenvs.create false \
    && poetry install --only main

EXPOSE 80 81

ENV PROMETHEUS_DISABLE_CREATED_SERIES=True
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]