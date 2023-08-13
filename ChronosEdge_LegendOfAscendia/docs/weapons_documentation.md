# Weapons Documentation

## Overview

In "Chronos Edge: Legend of Ascendia", weapons play a crucial role in the gameplay. They are not only tools for combat but also a means to interact with the environment and solve puzzles. This document provides an overview of the `Weapon` data schema and its usage in the game.

## Weapon Data Schema

The `Weapon` data schema is defined in the `weapons.py` file. Each weapon has the following attributes:

- `name`: The name of the weapon.
- `damage`: The amount of damage the weapon can inflict.
- `range`: The effective range of the weapon.
- `special_ability`: The special ability of the weapon, if any.
- `owner`: The `Character` who owns the weapon.

## Weapon Usage

Weapons are primarily used in combat scenarios. The `Character` class in `character.py` has a `weapon` attribute that holds the current weapon of the character. The `attack()` method in the `Character` class uses the `damage` attribute of the weapon to calculate the damage inflicted on enemies.

Weapons can also be used to interact with the environment. For example, some weapons can be used to break barriers, activate switches, or solve puzzles. The `interact()` method in the `Environment` class in `environments.py` checks the `special_ability` of the weapon to determine the outcome of the interaction.

## Special Abilities

Some weapons have special abilities that can manipulate time, gravity, or other aspects of the game world. These abilities are powered by the Havok Physics engine and are defined in the `physics.py` file. The `use_ability()` method in the `Weapon` class triggers the special ability of the weapon.

## Multiplayer Usage

In multiplayer mode, players can trade weapons or team up to use their weapons in coordinated attacks. The `trade()` and `team_attack()` methods in the `multiplayer.py` file handle these interactions.

## PvP Arena

In the PvP arena, players can test their skills against each other using their weapons. The `startPvP()` function in `pvp_arena.py` initiates a PvP match, and the `fight()` method in the `Character` class handles the combat mechanics.

## Demo

The demo showcases the variety of weapons and their uses in the game. The `startDemo()` function in `demo.py` sets up a series of scenarios to demonstrate the weapons' capabilities.