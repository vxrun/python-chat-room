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
