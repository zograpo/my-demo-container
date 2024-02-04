FROM debian:latest

WORKDIR /myapp

RUN apt-get update && apt-get install -y python3

COPY my_app.py .

RUN mkdir logs

CMD ["python3", "my_app.py"]
