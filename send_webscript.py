import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='router',
                         exchange_type='direct')

routing_key = 'webscript'
message = sys.argv[1]
channel.basic_publish(exchange='router',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()