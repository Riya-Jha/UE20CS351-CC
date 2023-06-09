FROM library/python:3.6-stretch

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN pip3 install -r requirements.txt

WORKDIR /healthcheck

COPY . /healthcheck

ENTRYPOINT [ "python3" ]

CMD [ "healthcheck.py" ]
