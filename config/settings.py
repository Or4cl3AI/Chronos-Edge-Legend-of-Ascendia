# config/settings.py

```python
class Settings:
    def __init__(self):
        self.game_title = "Chronos Edge: Legend of Ascendia"
        self.engine = "Unreal Engine 5"
        self.physics_engine = "Havok Physics"
        self.multiplayer_enabled = True
        self.demo_mode = True

        # Graphics settings
        self.resolution = (1920, 1080)
        self.fullscreen = True
        self.vsync = True
        self.fps_limit = 60

        # Sound settings
        self.master_volume = 100
        self.music_volume = 80
        self.sfx_volume = 80
        self.voiceover_volume = 80

        # Gameplay settings
        self.difficulty = "Normal"
        self.auto_save = True
        self.subtitles = True

gameSettings = Settings()
```