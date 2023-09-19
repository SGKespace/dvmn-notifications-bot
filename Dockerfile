FROM python:3.10-slim-buster
MAINTAINER sgk
WORKDIR /opt/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /opt/app
CMD [ "python3", "./bot.py"]