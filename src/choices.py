```python
class Choice:
    def __init__(self, id, text, consequences):
        self.id = id
        self.text = text
        self.consequences = consequences

class ChoiceSchema:
    def __init__(self):
        self.choices = []

    def add_choice(self, id, text, consequences):
        self.choices.append(Choice(id, text, consequences))

    def get_choice(self, id):
        for choice in self.choices:
            if choice.id == id:
                return choice
        return None

def make_choice(choice_id):
    global currentChoice
    choice = ChoiceSchema().get_choice(choice_id)
    if choice:
        currentChoice = choice
        for consequence in choice.consequences:
            apply_consequence(consequence)
        return True
    return False

def apply_consequence(consequence):
    # This function will apply the consequence of a choice.
    # The implementation of this function will depend on the game's mechanics.
    pass
```