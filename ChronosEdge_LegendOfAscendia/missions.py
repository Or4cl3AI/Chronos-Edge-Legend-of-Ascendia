```python
import random
from character import Character
from enemies import Enemy
from weapons import Weapon

class Mission:
    def __init__(self, name, description, difficulty, enemies, reward):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.enemies = enemies
        self.reward = reward

    def startMission(self, player: Character):
        print(f"Starting mission: {self.name}")
        print(self.description)

        for enemy in self.enemies:
            while player.health > 0 and enemy.health > 0:
                player.attack(enemy)
                if enemy.health > 0:
                    enemy.attack(player)

        if player.health > 0:
            print(f"Mission {self.name} completed!")
            player.inventory.append(self.reward)
        else:
            print("You have been defeated. Try again.")

def generate_missions():
    missions = []
    enemy = Enemy("Goblin", 100, Weapon("Sword", 10, 2))
    missions.append(Mission("Goblin Hunt", "Defeat the goblin.", 1, [enemy], "Goblin Sword"))
    return missions

def startMission(mission: Mission, player: Character):
    mission.startMission(player)

if __name__ == "__main__":
    player = Character("Player", 100, Weapon("Sword", 10, 2))
    missions = generate_missions()
    startMission(random.choice(missions), player)
```