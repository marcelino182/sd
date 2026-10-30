import pika
import sys

def callback(ch, method, properties, body):
    print(f" [x] Recebido do Stream: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    credentials = pika.PlainCredentials('aluno', 'aluno')
    parameters = pika.ConnectionParameters(
        host='localhost',          
        virtual_host='/my_vhost',   
        credentials=credentials
    )

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    STREAM_NAME = 'meu_stream_de_eventos'

    # COMENTADO: Removemos o queue_declare do consumidor. 
    # Como o produtor já rodou, o stream já existe. Sem declarar, evitamos o erro 530 de falta de permissão de configuração.
    # channel.queue_declare(queue=STREAM_NAME, durable=True, arguments={"x-queue-type": "stream"})

    # Configuração obrigatória de QoS para Streams
    channel.basic_qos(prefetch_count=100)

    # Configura para ler todo o histórico
    opcoes_consumo = {
        "x-stream-offset": "first" 
    }

    # Inicia o consumo direto
    channel.basic_consume(
        queue=STREAM_NAME,
        on_message_callback=callback,
        auto_ack=False, 
        arguments=opcoes_consumo
    )

    print(' [*] Aguardando mensagens do Stream em my_vhost. Para sair pressione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[-] Encerrando consumidor...')
        sys.exit(0)
