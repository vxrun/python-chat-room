import socket
import threading

host = '127.0.0.1'  # localHost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} left the chat'.encode('ascii'))


def receive():
    while True:
        client, address = server.accept()
        print(f'connected! with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        clients.append(client)

        print(f'Nickname of Client is {nickname}')
        broadcast(f'{nickname} joined the chat! '.encode('ascii'))
        client.send(f'Connected to the server! '.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is listening !")
receive()
