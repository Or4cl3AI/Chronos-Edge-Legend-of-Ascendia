```python
class Character:
    def __init__(self, name, health, strength, agility, weapons):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.weapons = weapons
        self.position = (0, 0, 0)  # x, y, z coordinates in the game world

    def move(self, x, y, z):
        self.position = (x, y, z)

    def attack(self, enemy):
        weapon = self.weapons[0]  # Assume the first weapon in the list is equipped
        damage = weapon.damage * self.strength
        enemy.health -= damage

    def equip_weapon(self, weapon):
        if weapon in self.weapons:
            self.weapons.remove(weapon)
            self.weapons.insert(0, weapon)

    def heal(self, amount):
        self.health += amount
        if self.health > 100:  # Assume the maximum health is 100
            self.health = 100

    def is_alive(self):
        return self.health > 0
```