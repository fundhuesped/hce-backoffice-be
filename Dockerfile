FROM python:3.6.8
ENV PYTHONUNBUFFERED 1
RUN pip3 install pip==9.0.1
RUN pip3 --version
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt --no-cache-dir
ADD . /code/
