from socket import * 
import threading
from constCS import *

def lidar_clientes(conn, addr):
    print("Cliente Conectado com sucesso", addr)
    while True: #loop para troca de dados com o cliente
            data = conn.recv(1024)
            if not data or data.decode() == 'fim': # se o cliente parou de enviar dados ou se enviou o fim 
                break
            msg = "Servidor: respondeu " + data.decode()
            conn.send(msg.encode()) # enviar a resposta
    conn.close() # sai do loop e encerra a conexao
    print("Conexão com", addr, 'fechada.')
print("Servidor iniciando")
s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True: #loop externo para aceitar conexões
     print("Aceitando Conexões")
     conn, addr = s.accept() # returna um novo socket caso um conexao chegue
     client_thread = threading.Thread(target=lidar_clientes,args=(conn,addr))
     client_thread.start()