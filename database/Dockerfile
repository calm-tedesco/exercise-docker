FROM mongo:latest

COPY container_2.py requirements.txt /
COPY start_container.sh /docker-entrypoint-initdb.d

RUN apt update && apt install -y python3 python3-pip
RUN pip3 install -r requirements.txt

CMD [ "mongod" ]
