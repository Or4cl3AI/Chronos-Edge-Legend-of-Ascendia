```python
import sys
from game_engine import UnrealEngine5
from character import Character
from weapons import Weapon
from environments import Environment
from enemies import Enemy
from physics import HavokPhysics
from multiplayer import Multiplayer
from storyline import Storyline
from dialogues import Dialogue
from choices import Choice
from missions import Mission
from pvp_arena import PvPArena
from demo import Demo

def initGame():
    print("Initializing Chronos Edge: Legend of Ascendia...")
    engine = UnrealEngine5()
    physics = HavokPhysics()
    environment = Environment(engine, physics)
    character = Character(engine, physics)
    weapon = Weapon(engine, physics)
    enemy = Enemy(engine, physics)
    multiplayer = Multiplayer()
    storyline = Storyline()
    dialogue = Dialogue()
    choice = Choice()
    mission = Mission(character, enemy, environment)
    pvp_arena = PvPArena(character, enemy)
    demo = Demo(engine, physics, environment, character, weapon, enemy, multiplayer, storyline, dialogue, choice, mission, pvp_arena)
    return demo

def startDemo(demo):
    print("Starting demo...")
    demo.start()

def main():
    demo = initGame()
    startDemo(demo)

if __name__ == "__main__":
    main()
```