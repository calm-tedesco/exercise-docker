FROM python:latest

COPY container_1.py requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./container_1.py" ]

