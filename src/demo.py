```python
import pygame
from src import game, characters, weapons, physics, levels, multiplayer, dialogues, choices, missions, arenas

# Initialize Pygame
pygame.init()

# Shared Variables
demoState = {
    "status": "not started",
    "currentScene": None,
    "currentCharacter": None,
    "currentWeapon": None,
    "currentPhysics": None,
    "currentLevel": None,
    "currentMultiplayer": None,
    "currentDialogue": None,
    "currentChoice": None,
    "currentMission": None,
    "currentArena": None,
}

def startDemo():
    demoState["status"] = "running"
    demoState["currentScene"] = game.gameState["currentScene"]
    demoState["currentCharacter"] = characters.playerCharacter
    demoState["currentWeapon"] = weapons.playerWeapon
    demoState["currentPhysics"] = physics.physicsState
    demoState["currentLevel"] = levels.currentLevel
    demoState["currentMultiplayer"] = multiplayer.multiplayerState
    demoState["currentDialogue"] = dialogues.currentDialogue
    demoState["currentChoice"] = choices.currentChoice
    demoState["currentMission"] = missions.currentMission
    demoState["currentArena"] = arenas.currentArena

    print("Demo started. Explore the world of Chronos Edge: Legend of Ascendia!")

def endDemo():
    demoState["status"] = "ended"
    print("Demo ended. Thank you for playing Chronos Edge: Legend of Ascendia!")

def updateDemo():
    if demoState["status"] == "running":
        game.updateGame()
        characters.updateCharacters()
        weapons.updateWeapons()
        physics.updatePhysics()
        levels.updateLevels()
        multiplayer.updateMultiplayer()
        dialogues.updateDialogues()
        choices.updateChoices()
        missions.updateMissions()
        arenas.updateArenas()

        print("Demo updated.")

def renderDemo():
    if demoState["status"] == "running":
        game.renderGame()
        characters.renderCharacters()
        weapons.renderWeapons()
        physics.renderPhysics()
        levels.renderLevels()
        multiplayer.renderMultiplayer()
        dialogues.renderDialogues()
        choices.renderChoices()
        missions.renderMissions()
        arenas.renderArenas()

        print("Demo rendered.")
```