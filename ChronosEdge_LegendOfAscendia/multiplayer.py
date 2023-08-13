```python
import socket
from threading import Thread
from character import Character
from missions import Mission
from pvp_arena import PvPArena

class Multiplayer:
    def __init__(self, host='localhost', port=55555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []
        self.characters = {}

    def broadcast(self, message, client):
        for c in self.clients:
            if c != client:
                c.send(message)

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message, client)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                character = self.characters[index]
                broadcast(f'{character.name} has left the game.')
                break

    def start_server(self):
        while True:
            client, address = self.server.accept()
            self.clients.append(client)
            character = Character()
            self.characters[self.clients.index(client)] = character
            print(f'Connected with {str(address)}')
            client.send('Connected to the server!'.encode('ascii'))
            thread = Thread(target=self.handle_client, args=(client,))
            thread.start()

    def start_mission(self, mission_id, player_ids):
        mission = Mission(mission_id)
        players = [self.characters[id] for id in player_ids]
        mission.start(players)

    def start_pvp(self, arena_id, player_ids):
        arena = PvPArena(arena_id)
        players = [self.characters[id] for id in player_ids]
        arena.start(players)

if __name__ == "__main__":
    multiplayer = Multiplayer()
    multiplayer.start_server()
```