FROM python:3

# RUN apt-get update -y && \
#     apt-get install -y python3-pip python3-dev

WORKDIR /deletion

RUN pip3 install -r requirements.txt

COPY . /deletion

ENTRYPOINT [ "python" ]

CMD [ "deletion.py" ]