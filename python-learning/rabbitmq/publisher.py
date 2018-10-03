#!/usr/bin/env python3

import pika
import sys

print('step 1')
connect = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connect.channel()

channel.queue_declare(queue='pika_queue')
channel.basic_publish(exchange='', 
        routing_key='pika_queue', 
        body='from publisher:hello pika\r\n')
print('publisher send : hello pika\r\n')

channel.close()

