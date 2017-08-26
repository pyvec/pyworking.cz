FROM python:3.6

MAINTAINER Petr Messner

ENV PYTHONUNBUFFERED 1

RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip wheel
RUN /venv/bin/pip install gunicorn

COPY requirements.txt /app/requirements.txt
RUN /venv/bin/pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app

RUN useradd --no-create-home app
USER app

EXPOSE 8000

CMD [ \
    "/venv/bin/gunicorn", \
    "--workers", "2", \
    "--bind", "0.0.0.0:8000", \
    "--preload", \
    "--max-requests", "100", \
    "pyworking_web:app" \
]
