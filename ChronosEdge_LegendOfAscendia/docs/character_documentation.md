# Character Documentation

## Overview

The `Character` class represents the player character in "Chronos Edge: Legend of Ascendia". This class is used to manage the character's attributes, skills, weapons, and interactions with the game world.

## Attributes

- `name`: The name of the character.
- `level`: The character's current level.
- `health`: The character's current health.
- `max_health`: The character's maximum health.
- `strength`: The character's strength attribute, affecting physical damage.
- `agility`: The character's agility attribute, affecting speed and evasion.
- `intelligence`: The character's intelligence attribute, affecting magic power and skill cooldowns.
- `weapon`: The character's currently equipped weapon. This is an instance of the `Weapon` class.
- `inventory`: A list of items currently carried by the character.

## Methods

- `__init__(self, name)`: Initializes a new character with the given name.
- `level_up(self)`: Increases the character's level by 1, and increases all attributes.
- `equip_weapon(self, weapon)`: Equips the given weapon to the character.
- `attack(self, enemy)`: Makes the character attack the given enemy.
- `take_damage(self, amount)`: Reduces the character's health by the given amount.
- `heal(self, amount)`: Increases the character's health by the given amount, up to the maximum health.
- `add_to_inventory(self, item)`: Adds the given item to the character's inventory.
- `remove_from_inventory(self, item)`: Removes the given item from the character's inventory.

## Usage

```python
from character import Character
from weapons import Weapon

# Create a new character
hero = Character("Artemis")

# Level up the character
hero.level_up()

# Equip a weapon
sword = Weapon("Excalibur", 10, 2)
hero.equip_weapon(sword)

# Attack an enemy
hero.attack(goblin)

# Take damage
hero.take_damage(5)

# Heal
hero.heal(10)

# Add to inventory
hero.add_to_inventory("Health Potion")

# Remove from inventory
hero.remove_from_inventory("Health Potion")
```

For more detailed information, please refer to the source code in `character.py`.