from socket  import *
from constCS import *
s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #- Mapear a porta de escuta
s.listen(8)           #- quantidade de conexoes em espera
print("Servidor Iniciado!")
print("Aguardando conexões")
(conn, addr) = s.accept()  # returns new socket and addr. client 
print("Cliente Conectado!")
while True:                # forever
  print("Recebendo mensagem...")
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  msg = "Servidor:"+data.decode()+"*"  # process the incoming data into a response
  conn.send(msg.encode())  # return the response
conn.close()               # close the connection
print("Servidor Encerrado")