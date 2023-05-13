FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="Ammad Khalid <ammadkhalid@systembound.com>"

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /app

CMD ["hypercorn", "web:app", "--bind", "0.0.0.0:80"]

