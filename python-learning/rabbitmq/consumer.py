#!/usr/bin/env python3

import pika
import sys

def consumer_callback(channel, method, properties, body):
    print('consumer recv: %s' % body)

connect = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connect.channel()

channel.queue_declare(queue='pika_queue')
channel.basic_consume(consumer_callback, queue='pika_queue')
print('consumer recv : hello pika\r\n')
channel.start_consuming()

channel.close()
