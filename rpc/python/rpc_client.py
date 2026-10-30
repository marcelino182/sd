import xmlrpc.client
import sys

# Conecta ao servidor RPC
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8000")

print("--- Cliente RPC Iniciado ---")
while True:
    try:
        # Captura os dados digitados pelo usuário durante a execução
        num1 = int(input("Digite o primeiro número: "))
          
         # Chama a função remota
        resultado = proxy.is_even(num1)
        if resultado == 0:
            resposta = "É ímpar"
        else:
            resposta = "É par"
        print(f"\nO resultado é: {resposta}")

        continuar = input("Digite 'sair' para encerrar ou pressione ENTER para continuar\n")
        if continuar == 'sair':
            print("Encerrando o cliente...")
            break  
    except ValueError:
        print("\nErro: Você deve digitar apenas números inteiros válidos.")
    except Exception as e:
        print(f"\nErro ao conectar ao servidor: {e}")

