# Sistemas Distribuídos
Disciplina Sistemas Distribuídos

## Prática 01 Cluster Load Balancer

Criar uma máquina virtual para ser o servidor de load balance
### executar o script cluster/haproxy.sh na máquina 

Criar vários servidor web apache2 

### executar o script web.sh nas máquinas
 Este script irá instalar o apache2 e substituir o arquivo index.html padrão ( faça um alteração para diferenciar cada servidor)
 
## Prática 02 Comunicação via Socket

Na pasta socket a 3 tipos de servidores e clientes
- **simples** : 
    - um servidor aguarda um conexão recebe um dado e depois encerrar (**server-book.py**) 
    - o cliente conectada envia um dado e encerra (**client-book.py**)
    - um arquivo de configuração está disponível para definir endereço ip, porta, servidor (**constCS.py**) 
- **sequencial**: 
    - o servidor agora suporta atender mais de um cliente porém de maneira sequencial, um cliente por vez. (**server.py**)
    - o cliente agora consegue enviar várias mensagem para o servidor e se quiser encerrar basta enviar a palavra **fim** que a sua conexão é encerrada pelo servidor. Liberando o servidor para atender o próximo cliente. (**client.py**)
    - um arquivo de configuração está disponível para definir endereço ip, porta, servidor (**constCS.py**)
- **thread (paralelo)**: 
   - o servidor suporta vários cliente simultaneamente graças a utilização do conceito de threads, que permite que as tarefa de interagir com os clientes sejam feitas por threads diferentes, enquanto o servidor continua aceitando novas conexões. (**server-thread.py**)
   - o cliente continua sendo o mesmo do modelo sequencial.(**client.py**)
   - um arquivo de configuração está disponível para definir endereço ip, porta, servidor (**constCS.py**)
  ## ATENÇÃO - sobre o arquivo de configuração constCS.py , dependendo de como você irá testar a comunicação entre o cliente e servidor fique a atendo as variáveis:
  - **HOST** = endereço IP utilizado no servidor para receber as conexões dos clientes. O valor deve ser preenchido entre aspas simples **''** .Alguns valores possíveis :
       - **''** = vazio, quer dizer qualquer endereço IP que esteja configurado no servidor, valor padrão
       - **'localhost'**  apenas processos locais ( rodando dentro do computador) poderão se conectar, recomendado quando só tem um computador para testar
       - **'A.B.C.D'** um endereço IP específico, os computadores que estiverem na mesma rede dele no caso de um IP Privado, ou qualquer computador na internet caso seja um IP público.
   - **PORT** = Um valor inteiro entre 0 - 65656, recomendação utilizar valores maiores que 1024, ou que não sejam utilizados por outros softwares ou programas, valor acima de 5000 são um boa escola. 50007 é o valor padrão.
   - **SERVER** = O endereço que o cliente vai utilizar para acessar o servidor. Valor padrão **'localhost'** para tester dentro da própria máquina, mas pode ser algum dos endereços IP configurados no servidor.

  # Para utilizar o script primeiramente instale o python3 nas máquinas que vão utilizar, para facilitar dentro da pasta socket há um script chamado config.sh para instalação do python3 no computador
