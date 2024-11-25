from socket  import *
from constCS import * #- definir HOST PORT
print("servidor iniciando, criando socket, mapeando")
s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #- Mapear a porta de escuta
s.listen(2)           #- quantidade de conexoes em espera
while True: #loop externo para aceitar conexões
    (conn, addr) = s.accept()  # returns new socket and addr. client 
    print('Aguardo Conexões')
    print('Cliente conectado com endereço', addr)

    while True:                # loop interno para troca de dados com os clientes
      data = conn.recv(1024)   # receive data from client
      #if not data: break       # stop if client stopped
      # se o data for igual a fim encerra a conexão do cliente atual

      if data.decode() == 'fim': break
      msg = data.decode()+"*"  # process the incoming data into a response
      conn.send(msg.encode())  # return the response
    conn.close()               # close the connection
