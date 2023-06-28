import pika
import json
import pymysql.cursors

name=input('Enter name')
age=int(input('Enter age'))
message = [name, age]
connection =  pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=json.dumps(message))
body=json.dumps(message)
result_type=type(body)
message_type=type(message)
print("type of message = ", message_type)
print("type of result = ", result_type)
print("[x] Sent data")
connection.close()