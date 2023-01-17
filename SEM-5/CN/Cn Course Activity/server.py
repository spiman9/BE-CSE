import threading
import socket

host = '127.0.0.1'  #localhost
port = 9987

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(host , port)
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
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname}left the chat!!!')
            nicknames.remove(nickname)
            break

def reciev():
    while True:
        client , address = server.accept()
        print(f"Connected with address {str(address)}!!!")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode




















