```python
# Weapon Options Configuration for "Chronos Edge: Legend of Ascendia"

class WeaponOptions:
    def __init__(self):
        self.weapon_damage = {
            "sword": 50,
            "axe": 60,
            "bow": 40,
            "spear": 55,
            "dagger": 35
        }

        self.weapon_speed = {
            "sword": 1.0,
            "axe": 0.8,
            "bow": 1.2,
            "spear": 0.9,
            "dagger": 1.3
        }

        self.weapon_range = {
            "sword": 1.0,
            "axe": 0.8,
            "bow": 1.5,
            "spear": 1.2,
            "dagger": 0.7
        }

        self.weapon_special_ability = {
            "sword": "double_strike",
            "axe": "heavy_strike",
            "bow": "long_shot",
            "spear": "pierce",
            "dagger": "quick_strike"
        }

    def get_weapon_damage(self, weapon):
        return self.weapon_damage.get(weapon, 0)

    def get_weapon_speed(self, weapon):
        return self.weapon_speed.get(weapon, 0)

    def get_weapon_range(self, weapon):
        return self.weapon_range.get(weapon, 0)

    def get_weapon_special_ability(self, weapon):
        return self.weapon_special_ability.get(weapon, "")

weapon_options = WeaponOptions()
```