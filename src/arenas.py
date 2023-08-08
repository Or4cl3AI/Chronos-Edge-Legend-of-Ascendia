```python
class Arena:
    def __init__(self, name, description, enemies):
        self.name = name
        self.description = description
        self.enemies = enemies

    def start_arena(self):
        print(f"Welcome to {self.name}. {self.description}")
        print("Prepare for battle!")

    def end_arena(self):
        print(f"You have conquered {self.name}. Well done, warrior!")

class PvP_Arena(Arena):
    def __init__(self, name, description, enemies, players):
        super().__init__(name, description, enemies)
        self.players = players

    def start_arena(self):
        super().start_arena()
        print("This is a PvP arena. May the best player win!")

    def end_arena(self):
        super().end_arena()
        print("The PvP battle has ended. Congratulations to the victor!")

def startArena(arena):
    arena.start_arena()

def endArena(arena):
    arena.end_arena()
```