from socket import *

serverPort = 3030
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

print("Servidor inicializado.")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Conexão estabelecida com: ", addr)
    while True:
        message = connectionSocket.recv(1024).decode()
        if message == "exit":
            responseMessage = "Encerrando conexão"
            connectionSocket.send(responseMessage.encode())
            break
        else:
            print("Cliente: ", message)
            responseMessage = input("Resposta: ")
            connectionSocket.send(responseMessage.encode())
    print ('Encerrando conexão com', addr)
    connectionSocket.close()
    exit()