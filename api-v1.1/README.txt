Esse projeto contém um backend para um API REST de um micro-serviço de lista de tarefas 
escrito em python e utilizando o framework flask, a principio sem banco de dados, sendo os dados armazenados em memória em um dicionário,  
- app.py 

o frontend é composto pelos arquivos
index.html, script.js , styles.css

o script.js consome os através de chamadas a API e recebidos os dados em formato JSON.

Para testar a API podemos utilizar softwares como cURL ou POSTMAN 

#ler todas as tarefas
curl -X GET http://localhost:5000/tasks
#ler uma tarefa especifica pelo id
curl -X GET http://localhost:5000/tasks/1
#gravar uma tarefa 
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Tarefa 1", "description": "nova tarefa dificil"}'
#exclui um tarefa
curl -X delete http://localhost:5000/tasks/1

#altera uma tarefa
 curl -X PUT http://localhost:5000/tasks/1 -H "Content-Type: application/json" -d '{"title": "Novo título", "description": "Nova descrição", "completed": true}'