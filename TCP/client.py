from socket import *

serverName = "localhost"
serverPort = 3030
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    clientSocket.connect((serverName, serverPort))
except:
    print("Não foi possível estabelecer conexão.")
    exit()
finally:
    print("Conexão estabelecida.")

while True:
    try:
        message = input("Digite a mensagem ('exit' para encerrar conexão):")
        clientSocket.send(message.encode())
        print("Aguardando resposta...")
        responseMessage = clientSocket.recv(1024).decode()
        print("Resposta do servidor: ", responseMessage)
        if responseMessage == "Encerrando conexão":
            clientSocket.close()
            exit()
    except:
        print("Conexão encerrada.")
        clientSocket.close()
        break
exit()