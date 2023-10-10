from socket import *
from threading import *
from random import randint, choice

serverPort = 12001

# Shared variable to control server termination
terminate_server = False

# Method to handle client-server communication
def handleClient(clientSocket, addr):
    global terminate_server
    while not terminate_server:
        sentence = clientSocket.recv(2048).decode()
        print('received: ' + sentence)
        splittetText = sentence.split()
        Text = ''

        if len(splittetText) == 0:
            continue  # Handle empty input gracefully

        if splittetText[0].lower() == 'add':
            talx = int(splittetText[1])
            taly = int(splittetText[2])
            Text = f'{talx} + {taly} = {(talx + taly)}'
        elif (splittetText[0].lower() == 'sub'):
            talx = int (splittetText[1])
            taly = int (splittetText[2]) 
            Text = f'{talx} - {taly} = {(talx - taly)}'
        elif splittetText[0].lower() == 'random':
            min_num = min(int(splittetText[1]), int(splittetText[2]))
            max_num = max(int(splittetText[1]), int(splittetText[2]))

            # Generate two random numbers within the provided range
            random_num1 = randint(min_num, max_num)
            random_num2 = randint(min_num, max_num)

            # Choose a random operation
            operation = choice(['add', 'sub', 'mul'])

            if operation == 'add':
                Text = f'{random_num1} + {random_num2} = {(random_num1 + random_num2)}'
            elif operation == 'sub':
                Text = f'{random_num2} - {random_num1} = {(random_num2 - random_num1)}'
            elif operation == 'mul':
                Text = f'{random_num1} * {random_num2} = {(random_num1 * random_num2)}'
        elif splittetText[0].lower() == 'close':
            terminate_server = True
            Text = 'Server is closing...'
        else:
            Text = f'Ugyldigt {splittetText[0]}'

        print('Sending back text to client: ' + Text)
        clientSocket.send(Text.encode())

    clientSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is up and running on the port', serverPort)

while not terminate_server:
    connectionSocket, addr = serverSocket.accept()
    print('Connected to client using address', addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()
