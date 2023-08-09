import socket
import threading
from django.src.game import gameState
from django.src.characters import playerCharacter

class MultiplayerServer:
    def __init__(self, host='localhost', port=55555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []
        self.nicknames = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f'{nickname} left the game!'.encode('ascii'))
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f'Nickname of the client is {nickname}!')
            self.broadcast(f'{nickname} joined the game!'.encode('ascii'))
            client.send('Connected to the server!'.encode('ascii'))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

class MultiplayerClient:
    def __init__(self, nickname, host='localhost', port=55555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname = nickname

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("An error occured!")
                self.client.close()
                break

    def write(self):
        while True:
            message = f'{self.nickname}: {input("")}'
            self.client.send(message.encode('ascii'))

    def start_client(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

def start_multiplayer_mode():
    nickname = playerCharacter.name
    client = MultiplayerClient(nickname)
    client.start_client()