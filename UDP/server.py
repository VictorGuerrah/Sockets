from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print('Servidor pronto para receber.')

while True:

    print('Aguardando...')

    message, clientAddress = serverSocket.recvfrom(2048)
    messageDecoded = message.decode()
    responseMessage = ""

    try:
        responseMessage = eval(messageDecoded)
    except:
        responseMessage = "Erro ao realizar a operação."
    finally:
        print("Enviando resposta...")
        serverSocket.sendto(str(responseMessage).encode(), clientAddress)


print("Fechando servidor...")
serverSocket.close()
