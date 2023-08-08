```python
import pygame
from src import game, characters, weapons, physics, levels, multiplayer, dialogues, choices, missions, arenas, demo
from config import settings, controls, game_options, graphics_options, sound_options, multiplayer_options, physics_options, character_options, weapon_options, level_options, dialogue_options, choice_options, mission_options, arena_options, demo_options

def main():
    pygame.init()

    gameSettings = settings.load()
    gameControls = controls.load()
    gameOptions = game_options.load()

    gameState = game.GameState()
    playerCharacter = characters.PlayerCharacter(character_options.load())

    currentLevel = None
    currentMission = None
    currentDialogue = None
    currentChoice = None
    currentArena = None
    demoState = None

    while gameState.is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState.is_running = False

        game.update(gameState, playerCharacter, gameSettings, gameControls, gameOptions)
        characters.update(playerCharacter)
        weapons.update(playerCharacter.weapon)
        physics.update(gameState, playerCharacter)
        
        if currentLevel:
            levels.update(currentLevel)
        if currentMission:
            missions.update(currentMission)
        if currentDialogue:
            dialogues.update(currentDialogue)
        if currentChoice:
            choices.update(currentChoice)
        if currentArena:
            arenas.update(currentArena)
        if demoState:
            demo.update(demoState)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
```