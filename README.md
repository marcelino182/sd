# Sistemas Distribuídos
Disciplina Sistemas Distribuídos

## Prática 01 Cluster Load Balancer

Criar uma máquina virtual para ser o servidor de load balance
### executar o script cluster/haproxy.sh na máquina 

Criar um servidor web apache 

### executar o script web.sh nas máquinas

## Prática 02 Comunicação via Socket

Na pasta socket a 3 tipos de servidores e clientes
- **simples** : 
    - um servidor aguarda um conexão recebe um dado e depois encerrar (server-book.py) 
    - o cliente conectada envia um dado e encerra (client-book.py)
    - um arquivo de configuração está disponível para definir endereço ip, porta, servidor (constCS.py) 
- **sequencial**: 
    - o servidor agora suporta atender mais de um cliente porém de maneira sequencial, um cliente por vez.
    - o cliente agora consegue enviar várias mensagem para o servidor e se quiser encerrar basta enviar a palavra **fim** que a sua conexão é encerrada pelo servidor. Liberando o servidor para atender o próximo cliente. 
    - um arquivo de configuração está disponível para definir endereço ip, porta, servidor (constCS.py)
- **thread (paralelo)**: 
   - o servidor suporta vários cliente simultaneamente graças a utilização do conceito de threads, que permite que as tarefa de interagir com os clientes sejam feitas por threads diferentes, enquanto o servidor continua aceitando novas conexões. 
   - o cliente continua sendo o mesmo do modelo sequencial.
   - um arquivo de configuração está disponível para definir endereço ip, porta, servidor (constCS.py)