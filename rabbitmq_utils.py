import pika
import json
from consts import EXCHANGE, QUEUE, ROUTING_KEY


def get_rabbitmq_connection():
    return pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq',
        port=5672,
        virtual_host='/',
        credentials=pika.PlainCredentials('guest', 'guest')))


def get_channel(connection):
    channel = connection.channel()
    # Create the exchange if it doesn't already exist:
    channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic', durable=True)
    return channel


def create_and_bind_queue(channel):
    channel.queue_declare(QUEUE)
    channel.queue_bind(QUEUE, EXCHANGE, ROUTING_KEY)


def publish_message(channel, message):
    channel.basic_publish(exchange=EXCHANGE,
                          routing_key=ROUTING_KEY,
                          body=json.dumps(message),
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ))

    print(f'Published message: {message}, to exchange {EXCHANGE}, routing key {ROUTING_KEY}')


def read_messages(callback):
    connection = get_rabbitmq_connection()
    channel = get_channel(connection)
    channel.basic_consume(
        queue=QUEUE,
        auto_ack=True,
        on_message_callback=callback)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()
