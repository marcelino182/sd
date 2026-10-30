import pika
import time

# 1. Conecta ao servidor local do RabbitMQ

credentials = pika.PlainCredentials(
    'aluno',
    'aluno'
)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        'localhost',
        5672,
        '/my_vhost',
        credentials
    )
)

channel = connection.channel()

# Nome da fila tipo Stream
STREAM_NAME = 'meu_stream_de_eventos'

# 2. Declara o Stream (O pulo do gato é o argumento "x-queue-type")
channel.queue_declare(
    queue=STREAM_NAME,
    durable=True, # Streams obrigatoriamente precisam ser duráveis
    arguments={"x-queue-type": "stream"}
)

print(f"[*] Stream '{STREAM_NAME}' verificado/criado.")

# 3. Publica algumas mensagens de teste no Stream
for i in range(1, 6):
    mensagem = f"Evento número {i} gerado em {time.strftime('%H:%M:%S')}"
    
    channel.basic_publish(
        exchange='',               # Exchange padrão do RabbitMQ
        routing_key=STREAM_NAME,   # Nome do Stream
        body=mensagem
    )
    print(f" [x] Enviado: '{mensagem}'")
    time.sleep(1) # Pausa de 1 segundo entre envios

# Fechar conexão de forma limpa
connection.close()
