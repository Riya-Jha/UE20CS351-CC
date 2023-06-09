FROM python:3

# RUN apt-get update -y && \
#     apt-get install -y python3-pip python3-dev

WORKDIR /insertion

RUN pip3 install -r requirements.txt

COPY . /insertion

ENTRYPOINT [ "python" ]

CMD [ "insertion.py" ]