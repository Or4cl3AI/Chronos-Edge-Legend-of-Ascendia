1. Shared Variables:
   - `gameState`: Holds the current state of the game.
   - `playerCharacter`: Stores the player's character data.
   - `gameSettings`: Contains the game's configuration settings.
   - `gameControls`: Stores the game's control settings.
   - `gameOptions`: Contains the game's options settings.
   - `currentLevel`: Holds the current level data.
   - `currentMission`: Stores the current mission data.
   - `currentDialogue`: Holds the current dialogue data.
   - `currentChoice`: Stores the current choice data.
   - `currentArena`: Holds the current arena data.
   - `demoState`: Contains the demo's state data.

2. Data Schemas:
   - `CharacterSchema`: Defines the structure of character data.
   - `WeaponSchema`: Defines the structure of weapon data.
   - `LevelSchema`: Defines the structure of level data.
   - `MissionSchema`: Defines the structure of mission data.
   - `DialogueSchema`: Defines the structure of dialogue data.
   - `ChoiceSchema`: Defines the structure of choice data.
   - `ArenaSchema`: Defines the structure of arena data.

3. DOM Element IDs:
   - `gameCanvas`: The main game display area.
   - `playerHUD`: The player's heads-up display.
   - `dialogueBox`: The area where dialogues are displayed.
   - `choiceBox`: The area where choices are displayed.
   - `missionStatus`: The area where mission status is displayed.
   - `arenaStatus`: The area where arena status is displayed.
   - `demoStatus`: The area where demo status is displayed.

4. Message Names:
   - `gameStart`: Signals the start of the game.
   - `gameEnd`: Signals the end of the game.
   - `levelStart`: Signals the start of a level.
   - `levelEnd`: Signals the end of a level.
   - `missionStart`: Signals the start of a mission.
   - `missionEnd`: Signals the end of a mission.
   - `dialogueStart`: Signals the start of a dialogue.
   - `dialogueEnd`: Signals the end of a dialogue.
   - `choiceMade`: Signals that a choice has been made.
   - `arenaStart`: Signals the start of an arena.
   - `arenaEnd`: Signals the end of an arena.
   - `demoStart`: Signals the start of the demo.
   - `demoEnd`: Signals the end of the demo.

5. Function Names:
   - `startGame()`: Starts the game.
   - `endGame()`: Ends the game.
   - `startLevel()`: Starts a level.
   - `endLevel()`: Ends a level.
   - `startMission()`: Starts a mission.
   - `endMission()`: Ends a mission.
   - `startDialogue()`: Starts a dialogue.
   - `endDialogue()`: Ends a dialogue.
   - `makeChoice()`: Makes a choice.
   - `startArena()`: Starts an arena.
   - `endArena()`: Ends an arena.
   - `startDemo()`: Starts the demo.
   - `endDemo()`: Ends the demo.