import pika
import time
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb")
db = client['studentdb']
collection = db["student"]
sleepTime = 20
time.sleep(sleepTime)
print('Consumer_four connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='read_database', durable=True)

def callback(ch, method, properties, body):
    ans = collection.find({})
    for document in ans:
        print(document)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    return "Database read"


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='read_database', on_message_callback=callback)
channel.start_consuming()