FROM python:3.12-slim

ARG UID=1000

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash -u $UID user

WORKDIR /app

RUN mkdir /app/static && mkdir /app/media && chmod 755 /app

COPY --chown=user:user requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=user:user . .

USER user

CMD ["gunicorn","-b","0.0.0.0:8000", "--worker-tmp-dir", "/tmp", "stud_lab.wsgi:application"]