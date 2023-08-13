```python
import UnrealEngine5
import HavokPhysics
from character import Character
from weapons import Weapon
from environments import Environment
from enemies import Enemy
from multiplayer import Multiplayer
from missions import Mission
from dialogues import Dialogue
from choices import Choice
from storyline import StorylineEvent
from pvp_arena import PvPArena

def startDemo():
    print("Welcome to the demo of Chronos Edge: Legend of Ascendia!")

    # Initialize game engine
    game_engine = UnrealEngine5()
    physics_engine = HavokPhysics()

    # Create demo character
    demo_character = Character("Demo Character", "Warrior", 100, 100)
    demo_weapon = Weapon("Demo Sword", 50, 10)
    demo_character.equip_weapon(demo_weapon)

    # Create demo environment
    demo_environment = Environment("Demo Environment", "Ancient Ruins", game_engine, physics_engine)

    # Create demo enemy
    demo_enemy = Enemy("Demo Enemy", "Monster", 100, 100)
    demo_enemy_weapon = Weapon("Monster Claw", 30, 5)
    demo_enemy.equip_weapon(demo_enemy_weapon)

    # Create demo mission
    demo_mission = Mission("Demo Mission", demo_character, demo_enemy, demo_environment)

    # Create demo dialogue
    demo_dialogue = Dialogue("Demo Dialogue", demo_character, demo_enemy)

    # Create demo choice
    demo_choice = Choice("Demo Choice", demo_dialogue, demo_character)

    # Create demo storyline event
    demo_storyline_event = StorylineEvent("Demo Event", demo_dialogue, demo_choice)

    # Create demo PvP arena
    demo_pvp_arena = PvPArena("Demo PvP Arena", demo_character, demo_enemy)

    # Create demo multiplayer
    demo_multiplayer = Multiplayer("Demo Multiplayer", demo_character, demo_enemy, demo_pvp_arena)

    # Start demo
    print("Starting demo...")
    demo_mission.startMission()
    demo_dialogue.engageDialogue()
    demo_choice.makeChoice()
    demo_multiplayer.startPvP()

    print("Demo completed. Thank you for playing Chronos Edge: Legend of Ascendia!")

if __name__ == "__main__":
    startDemo()
```