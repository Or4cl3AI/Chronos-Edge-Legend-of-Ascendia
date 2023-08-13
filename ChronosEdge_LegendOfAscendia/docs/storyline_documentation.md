# Storyline Documentation

## Overview

The storyline in "Chronos Edge: Legend of Ascendia" is a rich and captivating narrative that immerses the player in a world of exhilaration and adventure. The player, as the chosen one, is destined to restore balance to a fractured world.

## StorylineEvent

The `StorylineEvent` class is used to represent key events in the game's storyline. Each `StorylineEvent` has a unique identifier, a description, and a list of `Dialogue` objects associated with it.

```python
class StorylineEvent:
    def __init__(self, id, description, dialogues):
        self.id = id
        self.description = description
        self.dialogues = dialogues
```

## Functions

### engageDialogue()

The `engageDialogue()` function is used to start a dialogue associated with a `StorylineEvent`. It takes a `Dialogue` object as an argument and returns the player's chosen `Choice`.

```python
def engageDialogue(dialogue):
    # Display dialogue options
    # Return player's choice
```

### makeChoice()

The `makeChoice()` function is used for the player to make a choice during a dialogue. It takes a `Choice` object as an argument and returns the outcome of the choice.

```python
def makeChoice(choice):
    # Apply choice effects
    # Return outcome
```

## Usage

To use the storyline functionality, import the `StorylineEvent`, `engageDialogue()`, and `makeChoice()` from the `storyline.py` file.

```python
from storyline import StorylineEvent, engageDialogue, makeChoice
```

Then, create `StorylineEvent` objects, engage in dialogues, and make choices as needed.

```python
# Create a StorylineEvent
event = StorylineEvent(id, description, dialogues)

# Engage in a dialogue
choice = engageDialogue(dialogue)

# Make a choice
outcome = makeChoice(choice)
```

## Dependencies

The storyline functionality depends on the `Dialogue` and `Choice` classes from the `dialogues.py` and `choices.py` files, respectively. Make sure to import these classes when using the storyline functionality.

```python
from dialogues import Dialogue
from choices import Choice
```