```python
import random
from HavokPhysics import PhysicsObject
from weapons import Weapon

class Enemy(PhysicsObject):
    def __init__(self, name, health, weapon, strength, speed):
        super().__init__(mass=strength, friction=0.5, restitution=0.5)
        self.name = name
        self.health = health
        self.weapon = weapon
        self.strength = strength
        self.speed = speed

    def attack(self, target):
        damage = self.weapon.damage * self.strength
        target.health -= damage
        return damage

    def move(self, direction):
        self.apply_force(direction * self.speed)

    def is_alive(self):
        return self.health > 0

def generate_enemy():
    names = ["Goblin", "Orc", "Troll", "Dragon", "Witch"]
    weapons = [Weapon("Sword", 10), Weapon("Axe", 15), Weapon("Bow", 8), Weapon("Staff", 12), Weapon("Dagger", 7)]
    name = random.choice(names)
    health = random.randint(50, 200)
    weapon = random.choice(weapons)
    strength = random.randint(1, 10)
    speed = random.randint(1, 10)
    return Enemy(name, health, weapon, strength, speed)
```