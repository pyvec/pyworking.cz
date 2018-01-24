FROM python:3.6-alpine

MAINTAINER Petr Messner

ENV PYTHONUNBUFFERED=1 DATA_DIR=/app/data

RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip wheel
RUN /venv/bin/pip install flask gunicorn pyyaml markdown

COPY setup.py MANIFEST.in /app/
COPY pyworking_cz /app/pyworking_cz

RUN /venv/bin/pip install /app

COPY data /app/data

RUN adduser -S app
USER app

EXPOSE 8000

CMD [ \
    "/venv/bin/gunicorn", \
    "--workers", "2", \
    "--bind", "0.0.0.0:8000", \
    "--preload", \
    "--max-requests", "100", \
    "pyworking_cz:app" \
]
