# config/level_options.py

```python
class LevelOptions:
    def __init__(self):
        self.level_difficulty = "medium"
        self.level_theme = "ancient ruins"
        self.level_size = "large"
        self.level_enemies = "standard"
        self.level_gravity = "normal"
        self.level_time_manipulation = False

    def set_level_difficulty(self, difficulty):
        self.level_difficulty = difficulty

    def set_level_theme(self, theme):
        self.level_theme = theme

    def set_level_size(self, size):
        self.level_size = size

    def set_level_enemies(self, enemies):
        self.level_enemies = enemies

    def set_level_gravity(self, gravity):
        self.level_gravity = gravity

    def enable_time_manipulation(self):
        self.level_time_manipulation = True

    def disable_time_manipulation(self):
        self.level_time_manipulation = False
```
