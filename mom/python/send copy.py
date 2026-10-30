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
channel.queue_declare(queue='Marcelino')

channel.basic_publish(
    exchange='',
    routing_key='Marcelino',
    body='De Eu para Eu Mesmo'
)

print(" [x] Mensagem enviada 'Eu'")

connection.close()
