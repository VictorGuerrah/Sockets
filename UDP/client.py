from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Digite a operação aritmética:')
clientSocket.sendto(message.encode(), (serverName, serverPort))

print("Esperando resposta do serivdor...")

responseMessage, serverAddress = clientSocket.recvfrom(2048)

print("Resposta do servidor: {}".format(responseMessage.decode()))
clientSocket.close()

