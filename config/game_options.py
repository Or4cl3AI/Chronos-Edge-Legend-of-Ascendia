# config/game_options.py

```python
class GameOptions:
    def __init__(self):
        self.difficulty = "Normal"
        self.language = "English"
        self.subtitles = True
        self.hud_display = True
        self.graphics_quality = "High"
        self.sound_volume = 100
        self.music_volume = 80
        self.voice_volume = 90
        self.sfx_volume = 100
        self.physics_detail = "High"
        self.multiplayer_mode = "Co-op"
        self.character_customization = True
        self.weapon_choice = "Default"
        self.level_selection = "Auto"
        self.dialogue_mode = "Auto"
        self.choice_mode = "Manual"
        self.mission_mode = "Story"
        self.arena_mode = "PvP"
        self.demo_mode = "On"

    def set_option(self, option, value):
        if hasattr(self, option):
            setattr(self, option, value)

    def get_option(self, option):
        if hasattr(self, option):
            return getattr(self, option)

gameOptions = GameOptions()
```
