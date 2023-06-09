FROM python:3

WORKDIR /read

RUN pip3 install -r requirements.txt

COPY . /read

ENTRYPOINT [ "python" ]

CMD [ "read.py" ]