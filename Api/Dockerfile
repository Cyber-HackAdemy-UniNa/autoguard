FROM python:3.9.2-alpine

WORKDIR /Api

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
 && python -m pip install -r requirements.txt

COPY . .

EXPOSE 2053

CMD gunicorn --bind 0.0.0.0:2053 --certfile=./ssl/fullchain.pem --log-level DEBUG --keyfile=./ssl/privkey.pem server:app
