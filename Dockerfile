FROM node:18 as dev

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install Django djangorestframework autopep8
USER node
