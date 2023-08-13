# Demo Documentation

## Overview

The demo of "Chronos Edge: Legend of Ascendia" is a condensed version of the game that showcases its innovative mechanics, immersive world, and captivating story. It is designed to give players a taste of the full gaming experience.

## Dependencies

The demo relies on several shared dependencies:

- UnrealEngine5
- HavokPhysics
- Character
- Weapon
- Environment
- Enemy
- PlayerID
- Mission
- Dialogue
- Choice
- StorylineEvent
- PvPArena
- Demo
- initGame()
- startMission()
- engageDialogue()
- makeChoice()
- startPvP()
- startDemo()

## Functions

### startDemo()

This function initializes the demo. It sets up the game environment, spawns the player character, and starts the first mission.

### initGame()

This function is called within startDemo() to initialize the game engine and physics engine.

### startMission()

This function is called within startDemo() to start the first mission of the demo.

### engageDialogue()

This function is called within startDemo() to start the first dialogue of the demo.

### makeChoice()

This function is called within startDemo() to allow the player to make their first choice in the demo.

### startPvP()

This function is called within startDemo() to start a PvP match in the demo.

## Demo Flow

The demo starts with the player character in a safe environment. The player is then guided through a series of events that showcase the game's mechanics, including combat, dialogue, choice-making, and PvP. The demo concludes with a teaser for the full game.

## File References

The demo.py file references several other files:

- main.py: for the main game loop
- character.py: for the player character data schema
- weapons.py: for the weapons data schema
- environments.py: for the game environments data schema
- enemies.py: for the enemy characters data schema
- multiplayer.py: for the multiplayer functionality
- missions.py: for the missions data schema
- dialogues.py: for the dialogues data schema
- choices.py: for the player choices data schema
- pvp_arena.py: for the PvP arenas data schema

## Conclusion

The demo is a crucial part of "Chronos Edge: Legend of Ascendia," as it gives players a glimpse into the game's world and mechanics. It is designed to be engaging and exciting, leaving players eager to explore the full game.