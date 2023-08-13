# Missions Documentation

## Overview

The `missions.py` file contains the logic and data structures related to the missions in "Chronos Edge: Legend of Ascendia". Missions are key gameplay elements where players engage in combat, exploration, and puzzle-solving to progress the story and earn rewards.

## Dependencies

- `Character` from `character.py`
- `Enemy` from `enemies.py`
- `PlayerID` from `multiplayer.py`

## Data Structures

### Mission

A `Mission` object represents a single mission in the game. It contains the following attributes:

- `mission_id`: A unique identifier for the mission.
- `name`: The name of the mission.
- `description`: A brief description of the mission.
- `objectives`: A list of objectives that the player must complete to finish the mission.
- `rewards`: The rewards that the player will receive upon completing the mission.
- `enemies`: A list of `Enemy` objects that the player will encounter during the mission.

## Functions

### startMission()

The `startMission()` function begins a mission. It takes a `Mission` object and a `PlayerID` as arguments. The function sets up the mission environment, spawns enemies, and updates the player's current mission status.

## Usage

To start a mission, import the `startMission()` function and call it with a `Mission` object and a `PlayerID`. The function will handle all the necessary setup and updates.

```python
from missions import startMission
from character import PlayerID

# Assume mission and player_id are defined
startMission(mission, player_id)
```

This will start the mission and update the player's current mission status. The player can then proceed to complete the mission objectives, fight enemies, and earn rewards.