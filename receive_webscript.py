import pika
import time
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='router',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='router',
                       queue=queue_name,
                       routing_key='webscript')

def callback(ch, method, properties, body):
    logs = open("logs.txt", "a")
    ts = time.time()
    ft = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(" [x] Received %r" % body)
    print(ft)
    print("\n")
    logs.write(" [x] Received %r\n" % body)
    logs.write(ft)
    logs.write("\n\n")
    logs.close()

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
