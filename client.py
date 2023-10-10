from socket import *

# Variables
servername = 'localhost'
serverport = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername, serverport))

while True:
    sentence = input('Indtast linje (or type "close" to exit): ')
    data = sentence.encode()
    clientSocket.send(data)

    if sentence.lower() == 'close':
        print('close command typed...')
        print('the server and the client is now terminating...')

    dataBack = clientSocket.recv(2048)
    sentenceBack = dataBack.decode()
    print('Modtaget tekst:', sentenceBack)

    if sentence.lower() == 'close':
        if sentenceBack.lower() == 'server is closing...':
            break

clientSocket.close()
