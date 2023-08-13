```python
class Choice:
    def __init__(self, id, text, consequences):
        self.id = id
        self.text = text
        self.consequences = consequences

def makeChoice(choice):
    print(f"You have chosen: {choice.text}")
    for consequence in choice.consequences:
        consequence.apply()

class Consequence:
    def __init__(self, character_changes, storyline_changes):
        self.character_changes = character_changes
        self.storyline_changes = storyline_changes

    def apply(self):
        for change in self.character_changes:
            change.apply()
        for change in self.storyline_changes:
            change.apply()

class CharacterChange:
    def __init__(self, character, attribute, value):
        self.character = character
        self.attribute = attribute
        self.value = value

    def apply(self):
        setattr(self.character, self.attribute, self.value)

class StorylineChange:
    def __init__(self, storyline, event):
        self.storyline = storyline
        self.event = event

    def apply(self):
        self.storyline.add_event(self.event)
```