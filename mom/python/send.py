import pika

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
channel.queue_declare(queue='luiz')

channel.basic_publish(
    exchange='',
    routing_key='luiz',
    body='Oi'
)

print(" [x] Mensagem enviada 'luiz'")

connection.close()
