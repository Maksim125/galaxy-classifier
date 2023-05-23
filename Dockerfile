FROM docker/python:3.10.11-slim as final

RUN \
apt install -qq && \
apt-get install -y linux-headers-generic libgl1 && \
ap-getinstall -yq --no-install-recommends libgtk2.0-dev

RUN \
    pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade poetry

WORKDIR /app

COPY /app /app

COPY poetry.lock /app
COPY pyproject.toml /app

RUN \
    poetry config virtualenvs.create false \
    && poetry install --only main

EXPOSE 80 81

ENV PROMETHEUS_DISABLE_CREATED_SERIES=True
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]