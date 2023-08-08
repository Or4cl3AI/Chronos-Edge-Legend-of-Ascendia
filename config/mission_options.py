# config/mission_options.py

```python
class MissionOptions:
    def __init__(self):
        self.cooperative_missions_enabled = True
        self.pvp_arenas_enabled = True
        self.mission_difficulty = 'medium'
        self.mission_timer_enabled = False
        self.mission_replayability = True
        self.mission_auto_save = True

    def enable_cooperative_missions(self):
        self.cooperative_missions_enabled = True

    def disable_cooperative_missions(self):
        self.cooperative_missions_enabled = False

    def enable_pvp_arenas(self):
        self.pvp_arenas_enabled = True

    def disable_pvp_arenas(self):
        self.pvp_arenas_enabled = False

    def set_mission_difficulty(self, difficulty):
        self.mission_difficulty = difficulty

    def enable_mission_timer(self):
        self.mission_timer_enabled = True

    def disable_mission_timer(self):
        self.mission_timer_enabled = False

    def enable_mission_replayability(self):
        self.mission_replayability = True

    def disable_mission_replayability(self):
        self.mission_replayability = False

    def enable_mission_auto_save(self):
        self.mission_auto_save = True

    def disable_mission_auto_save(self):
        self.mission_auto_save = False


mission_options = MissionOptions()
```