# Dialogues Documentation

This document provides a detailed explanation of the `Dialogue` data schema and the `engageDialogue()` function used in the "Chronos Edge: Legend of Ascendia" game.

## Dialogue Data Schema

The `Dialogue` data schema is used to represent dialogues in the game. Each dialogue is an instance of the `Dialogue` class, which is defined in the `dialogues.py` file.

Here is a brief overview of the `Dialogue` class:

```python
class Dialogue:
    def __init__(self, id, text, choices):
        self.id = id
        self.text = text
        self.choices = choices
```

- `id`: A unique identifier for the dialogue.
- `text`: The text of the dialogue.
- `choices`: A list of `Choice` objects representing the choices the player can make in response to the dialogue.

## engageDialogue() Function

The `engageDialogue()` function is used to start a dialogue in the game. It is defined in the `dialogues.py` file and is used in the `storyline.py` and `choices.py` files.

Here is a brief overview of the `engageDialogue()` function:

```python
def engageDialogue(dialogue):
    print(dialogue.text)
    for choice in dialogue.choices:
        print(choice.text)
```

- `dialogue`: The `Dialogue` object representing the dialogue to be engaged.
- The function first prints the text of the dialogue.
- Then, it iterates over the choices in the dialogue and prints the text of each choice.

Please refer to the `dialogues.py` file for the complete code and the `choices_documentation.md` file for more information about the `Choice` data schema.