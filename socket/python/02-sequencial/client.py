from socket  import *
from constCS import * #- definir endereço IP do servidor e porta
print("cliente iniciando, criando socket, se conectando")
s = socket(AF_INET, SOCK_STREAM)
s.connect((SERVER, PORT)) # connect to server (block until accepted)
print("cliente conectado ao servidor e porta", HOST, PORT)
while True:# loop para troca de dados com o servidor
# ler a mensagem a partir da entrada no teclado
  msg = input('Digite a mensagem: ')
#msg = "Hello World"     # compose a message
  s.send(msg.encode())    # send the message
  data = s.recv(1024)     # receive the response
  print(data.decode())    # print the result
#se o client escrever fim encerra a conexao
  if msg == 'fim':
    break

s.close()               # close the connection
