FROM python:slim-bullseye
WORKDIR /model 
COPY . .
COPY requirements.txt /model/requirements.txt
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean
RUN pip3 install --user -r requirements.txt
CMD ["/bin/sh"]