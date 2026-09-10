FROM python:3.12-slim AS build

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install  \
    -r requirements.txt

FROM python:3.12-slim AS runtime

RUN useradd --create-home --uid 1001 appuser

WORKDIR /app

COPY --from=build /install /usr/local
COPY app.py .
COPY test_app.py .

USER 1001

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=12s --retries=5 \
   CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8080/healthz', timeout=3)"]

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]