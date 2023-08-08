```python
import pygame
from src import characters, weapons, physics, levels, multiplayer, dialogues, choices, missions, arenas, demo
from config import settings, controls, game_options, graphics_options, sound_options, multiplayer_options, physics_options, character_options, weapon_options, level_options, dialogue_options, choice_options, mission_options, arena_options, demo_options

class Game:
    def __init__(self):
        pygame.init()
        self.gameState = None
        self.playerCharacter = None
        self.gameSettings = settings.GameSettings()
        self.gameControls = controls.GameControls()
        self.gameOptions = game_options.GameOptions()
        self.currentLevel = None
        self.currentMission = None
        self.currentDialogue = None
        self.currentChoice = None
        self.currentArena = None
        self.demoState = None

    def startGame(self):
        self.gameState = "gameStart"
        self.playerCharacter = characters.PlayerCharacter(character_options.CharacterOptions())
        self.currentLevel = levels.Level(level_options.LevelOptions())
        self.currentMission = missions.Mission(mission_options.MissionOptions())
        self.currentDialogue = dialogues.Dialogue(dialogue_options.DialogueOptions())
        self.currentChoice = choices.Choice(choice_options.ChoiceOptions())
        self.currentArena = arenas.Arena(arena_options.ArenaOptions())
        self.demoState = demo.Demo(demo_options.DemoOptions())

    def endGame(self):
        self.gameState = "gameEnd"

    def startLevel(self):
        self.gameState = "levelStart"
        self.currentLevel.start()

    def endLevel(self):
        self.gameState = "levelEnd"
        self.currentLevel.end()

    def startMission(self):
        self.gameState = "missionStart"
        self.currentMission.start()

    def endMission(self):
        self.gameState = "missionEnd"
        self.currentMission.end()

    def startDialogue(self):
        self.gameState = "dialogueStart"
        self.currentDialogue.start()

    def endDialogue(self):
        self.gameState = "dialogueEnd"
        self.currentDialogue.end()

    def makeChoice(self, choice):
        self.gameState = "choiceMade"
        self.currentChoice.make(choice)

    def startArena(self):
        self.gameState = "arenaStart"
        self.currentArena.start()

    def endArena(self):
        self.gameState = "arenaEnd"
        self.currentArena.end()

    def startDemo(self):
        self.gameState = "demoStart"
        self.demoState.start()

    def endDemo(self):
        self.gameState = "demoEnd"
        self.demoState.end()

if __name__ == "__main__":
    game = Game()
    game.startGame()
```