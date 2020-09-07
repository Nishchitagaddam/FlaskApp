FROM python:3.6
ADD . /flask_application
WORKDIR /flask_application
RUN pip install -r requirements.txt
