```python
class Dialogue:
    def __init__(self, id, text, character_id):
        self.id = id
        self.text = text
        self.character_id = character_id

class DialogueSchema:
    def __init__(self):
        self.dialogues = []

    def add_dialogue(self, dialogue):
        self.dialogues.append(dialogue)

    def get_dialogue(self, id):
        for dialogue in self.dialogues:
            if dialogue.id == id:
                return dialogue
        return None

def startDialogue(dialogue_id):
    global currentDialogue
    currentDialogue = DialogueSchema().get_dialogue(dialogue_id)
    if currentDialogue is not None:
        print(currentDialogue.text)

def endDialogue():
    global currentDialogue
    currentDialogue = None
```