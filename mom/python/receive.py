import signal
import pika

signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)

credentials = pika.PlainCredentials(
    'aluno',
    'aluno'
)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        '192.168.204.140',
        5672,
        '/my_vhost',
        credentials
    )
)

channel = connection.channel()
channel.queue_declare(queue='Marcelino')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body
)

channel.basic_consume('Marcelino', callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
