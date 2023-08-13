```python
from dialogues import Dialogue
from choices import Choice

class StorylineEvent:
    def __init__(self, id, dialogues, choices):
        self.id = id
        self.dialogues = dialogues
        self.choices = choices

    def start_event(self):
        for dialogue in self.dialogues:
            dialogue.display_dialogue()
        for choice in self.choices:
            choice.display_choice()

class Storyline:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def start_storyline(self):
        for event in self.events:
            event.start_event()

# Sample usage
storyline = Storyline()

# Create dialogues
dialogue1 = Dialogue("Character1", "Hello, warrior.")
dialogue2 = Dialogue("Character2", "Hello, friend.")

# Create choices
choice1 = Choice("Help Character1", "You decided to help Character1.")
choice2 = Choice("Help Character2", "You decided to help Character2.")

# Create an event
event = StorylineEvent(1, [dialogue1, dialogue2], [choice1, choice2])

# Add event to storyline
storyline.add_event(event)

# Start the storyline
storyline.start_storyline()
```