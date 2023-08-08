# config/choice_options.py

```python
class ChoiceOptions:
    def __init__(self):
        self.choice_time_limit = 30  # Time limit to make a choice in seconds
        self.choice_display_style = "list"  # Style of displaying choices: "list" or "grid"
        self.choice_highlight_color = (255, 255, 255)  # Color to highlight the selected choice

    def set_choice_time_limit(self, time_limit):
        self.choice_time_limit = time_limit

    def set_choice_display_style(self, display_style):
        self.choice_display_style = display_style

    def set_choice_highlight_color(self, color):
        self.choice_highlight_color = color

choice_options = ChoiceOptions()
```