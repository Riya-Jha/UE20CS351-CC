import pika
import time
from pymongo.mongo_client import MongoClient

# app = Flask(__name__)
client = MongoClient("mongodb")
db = client['studentdb']
collection = db["student"]

sleepTime = 20
time.sleep(sleepTime)
print('Consumer_two connecting to server ...')
started = False
while not started:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        started = True
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent. Waiting for sometime..")
        time.sleep(5)
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='insert_record', durable=True)


def callback(ch, method, properties, body):
    b = body.decode()
    b1 = b.split(".")
    x = b1[0]
    y = b1[1]
    z = b1[2]
    dict1 = {"SRN": x, "Name": y, "Section": z}
    collection.insert_one(dict1)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Student saved successfully!")


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='insert_record', on_message_callback=callback)
channel.start_consuming()
