```python
class Weapon:
    def __init__(self, name, damage, speed, special_ability):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.special_ability = special_ability

    def use(self, target):
        target.hp -= self.damage
        print(f"{self.name} used on {target.name}. {target.name} took {self.damage} damage.")

    def special(self, target):
        if self.special_ability:
            self.special_ability.use(target)
        else:
            print(f"{self.name} has no special ability.")

class SpecialAbility:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, target):
        self.effect(target)
        print(f"Special ability {self.name} used on {target.name}.")

def time_bend(target):
    target.speed /= 2
    print(f"{target.name}'s speed was halved by Time Bend.")

def legend_strike(target):
    target.hp -= 100
    print(f"{target.name} took 100 damage from Legend Strike.")

# Example usage:

# Define some special abilities
time_bend_ability = SpecialAbility("Time Bend", time_bend)
legend_strike_ability = SpecialAbility("Legend Strike", legend_strike)

# Define some weapons
sword = Weapon("Sword", 50, 10, time_bend_ability)
bow = Weapon("Bow", 30, 20, legend_strike_ability)

# Use weapons on some target (assuming target is an instance of Character)
sword.use(target)
bow.special(target)
```