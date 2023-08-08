```python
class Level:
    def __init__(self, level_data):
        self.level_data = level_data
        self.level_id = level_data['level_id']
        self.level_name = level_data['level_name']
        self.level_description = level_data['level_description']
        self.level_difficulty = level_data['level_difficulty']
        self.level_enemies = level_data['level_enemies']
        self.level_rewards = level_data['level_rewards']

    def start_level(self):
        print(f"Starting level: {self.level_name}")
        # Code to initialize the level goes here

    def end_level(self):
        print(f"Ending level: {self.level_name}")
        # Code to end the level goes here

class LevelManager:
    def __init__(self):
        self.levels = []
        self.current_level = None

    def load_levels(self, levels_data):
        for level_data in levels_data:
            self.levels.append(Level(level_data))

    def start_level(self, level_id):
        for level in self.levels:
            if level.level_id == level_id:
                self.current_level = level
                self.current_level.start_level()
                break

    def end_current_level(self):
        if self.current_level:
            self.current_level.end_level()
            self.current_level = None

level_manager = LevelManager()
```