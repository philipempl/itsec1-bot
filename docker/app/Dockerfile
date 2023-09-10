# Builder stage: Build the virtual environment
FROM python:3.11-slim-buster as builder

RUN apt-get update && apt-get install -y git

RUN pip install --upgrade typing-extensions

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY docker/app/pyproject.toml docker/app/poetry.lock ./

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# Runtime stage: Run the code using the virtual environment
FROM python:3.11-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

COPY ./app /app/app
COPY ./.streamlit /app/.streamlit

CMD ["streamlit", "run", "app/main.py", "--server.port=8080"]
