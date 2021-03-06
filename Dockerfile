
FROM python:3.6-jessie
MAINTAINER chnyun010@gmail.com 

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/usr/src/app

COPY . /usr/src/app

CMD ["python", "run.py"]