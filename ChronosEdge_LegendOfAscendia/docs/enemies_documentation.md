# Enemies Documentation

## Overview

In "Chronos Edge: Legend of Ascendia", enemies play a crucial role in challenging the player and driving the narrative forward. This document provides an overview of the `Enemy` data schema and its associated functionalities.

## Enemy Data Schema

The `Enemy` data schema is defined in the `enemies.py` file and is used across various modules of the game. It includes the following attributes:

- `name`: The name of the enemy.
- `health`: The current health of the enemy.
- `strength`: The strength of the enemy, determining the damage it can inflict.
- `defense`: The defense of the enemy, determining how much damage it can withstand.
- `weapon`: The weapon wielded by the enemy, an instance of the `Weapon` data schema.
- `isBoss`: A boolean indicating whether the enemy is a boss character.

## Enemy Behaviors

Enemies in "Chronos Edge: Legend of Ascendia" exhibit a range of behaviors, powered by the Unreal Engine 5 and Havok Physics engine. These behaviors are defined in the `enemies.py` file and include:

- `attack()`: Function for the enemy to attack the player.
- `defend()`: Function for the enemy to defend against the player's attack.
- `move()`: Function for the enemy to move within the environment.
- `die()`: Function to handle the enemy's death.

## Enemy Types

There are various types of enemies in the game, each with unique attributes and behaviors. These include:

- `StandardEnemy`: The most common type of enemy.
- `EliteEnemy`: A stronger enemy type with higher health, strength, and defense.
- `BossEnemy`: The most powerful enemy type, encountered at key points in the storyline.

## Interaction with Other Modules

The `Enemy` data schema and its associated functionalities interact with several other modules, including:

- `Character`: The player character engages in combat with enemies.
- `Weapon`: Enemies can wield weapons to attack the player.
- `Environment`: Enemies move and interact within game environments.
- `Missions`: Enemies are encountered during missions.
- `PvPArena`: Enemies may appear in PvP arenas for added challenge.

For more details on these interactions, refer to the respective documentation files.