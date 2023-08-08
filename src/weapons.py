```python
class Weapon:
    def __init__(self, name, damage, speed, special_ability):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.special_ability = special_ability

class WeaponSchema:
    def __init__(self):
        self.schema = {
            "name": "",
            "damage": 0,
            "speed": 0,
            "special_ability": ""
        }

    def validate(self, weapon):
        for key in self.schema.keys():
            if key not in weapon:
                return False
        return True

def load_weapons():
    weapons = []
    try:
        with open('assets/weapons.json', 'r') as f:
            data = json.load(f)
            for weapon in data:
                if WeaponSchema().validate(weapon):
                    weapons.append(Weapon(**weapon))
    except FileNotFoundError:
        print("Weapons file not found.")
    return weapons

def get_weapon(weapon_name):
    weapons = load_weapons()
    for weapon in weapons:
        if weapon.name == weapon_name:
            return weapon
    return None
```