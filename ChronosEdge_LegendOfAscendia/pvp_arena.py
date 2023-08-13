```python
import random
from character import Character
from enemies import Enemy

class PvPArena:
    def __init__(self, player1: Character, player2: Character):
        self.player1 = player1
        self.player2 = player2
        self.turn = random.choice([self.player1, self.player2])

    def startPvP(self):
        print(f"{self.turn.name} starts the PvP match!")
        while self.player1.hp > 0 and self.player2.hp > 0:
            if self.turn == self.player1:
                self.player2.hp -= self.player1.attack()
                self.turn = self.player2
            else:
                self.player1.hp -= self.player2.attack()
                self.turn = self.player1
            self.status()

        if self.player1.hp <= 0:
            print(f"{self.player2.name} wins the PvP match!")
        else:
            print(f"{self.player1.name} wins the PvP match!")

    def status(self):
        print(f"{self.player1.name} HP: {self.player1.hp}, {self.player2.name} HP: {self.player2.hp}")

if __name__ == "__main__":
    player1 = Character("Player1", 100, 20)
    player2 = Character("Player2", 100, 20)
    arena = PvPArena(player1, player2)
    arena.startPvP()
```