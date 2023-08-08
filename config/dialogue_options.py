# This is the configuration file for dialogue options in the game

class DialogueOptions:
    def __init__(self):
        # Maximum length of a dialogue
        self.max_length = 500

        # Minimum length of a dialogue
        self.min_length = 1

        # Time delay between dialogues
        self.dialogue_delay = 2.0

        # Enable or disable dialogue skipping
        self.allow_skip = True

        # Enable or disable dialogue fast-forwarding
        self.allow_fast_forward = True

        # Enable or disable dialogue rewind
        self.allow_rewind = False

        # Enable or disable dialogue pausing
        self.allow_pause = True

        # Enable or disable dialogue auto-advance
        self.auto_advance = False

        # Speed of dialogue auto-advance
        self.auto_advance_speed = 1.0

        # Enable or disable dialogue voiceover
        self.voiceover_enabled = True

        # Volume of dialogue voiceover
        self.voiceover_volume = 1.0

        # Enable or disable dialogue subtitles
        self.subtitles_enabled = True

        # Font size of dialogue subtitles
        self.subtitles_font_size = 16

        # Color of dialogue subtitles
        self.subtitles_color = "#FFFFFF"

        # Background color of dialogue subtitles
        self.subtitles_background_color = "#000000"

        # Opacity of dialogue subtitles background
        self.subtitles_background_opacity = 0.5

        # Enable or disable dialogue choices
        self.choices_enabled = True

        # Time limit for dialogue choices
        self.choices_time_limit = 30.0

        # Enable or disable dialogue choices countdown
        self.choices_countdown_enabled = True

        # Color of dialogue choices countdown
        self.choices_countdown_color = "#FF0000"

        # Enable or disable dialogue choices confirmation
        self.choices_confirmation_enabled = True

        # Text of dialogue choices confirmation
        self.choices_confirmation_text = "Are you sure?"

        # Enable or disable dialogue choices cancellation
        self.choices_cancellation_enabled = True

        # Text of dialogue choices cancellation
        self.choices_cancellation_text = "Cancel"