# config/demo_options.py

```python
class DemoOptions:
    def __init__(self):
        self.demo_enabled = True
        self.demo_duration = 30  # Duration of the demo in minutes
        self.demo_level = 'Tutorial'  # The level to be played in the demo
        self.demo_character = 'Chosen One'  # The character to be used in the demo
        self.demo_weapon = 'Time Blade'  # The weapon to be used in the demo
        self.demo_mission = 'Restore Balance'  # The mission to be played in the demo
        self.demo_arena = 'Ancient Ruins'  # The arena to be used in the demo
        self.demo_dialogue = 'Intro'  # The dialogue to be used in the demo
        self.demo_choice = 'Accept Destiny'  # The choice to be made in the demo

    def get_demo_options(self):
        return {
            'demo_enabled': self.demo_enabled,
            'demo_duration': self.demo_duration,
            'demo_level': self.demo_level,
            'demo_character': self.demo_character,
            'demo_weapon': self.demo_weapon,
            'demo_mission': self.demo_mission,
            'demo_arena': self.demo_arena,
            'demo_dialogue': self.demo_dialogue,
            'demo_choice': self.demo_choice
        }

demo_options = DemoOptions()
```
