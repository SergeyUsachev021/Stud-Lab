FROM python:3.12-slim

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash user

WORKDIR /user

RUN mkdir /user/static && mkdir /user/media && chown -R user:user /user && chmod 755 /user

COPY --chown=user:user . .

RUN pip install -r requirements.txt

USER user

CMD ["gunicorn","--control-socket","/tmp/stud_lab.ctl","-b","0.0.0.0:8000", "--worker-tmp-dir", "/tmp", "stud_lab.wsgi:application"]