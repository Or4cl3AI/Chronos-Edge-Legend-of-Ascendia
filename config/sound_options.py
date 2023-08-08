# Sound options configuration for "Chronos Edge: Legend of Ascendia"

class SoundOptions:
    def __init__(self):
        self.music_volume = 0.5
        self.sfx_volume = 0.5
        self.voiceover_volume = 0.5
        self.master_volume = 1.0

    def set_music_volume(self, volume):
        self.music_volume = volume

    def set_sfx_volume(self, volume):
        self.sfx_volume = volume

    def set_voiceover_volume(self, volume):
        self.voiceover_volume = volume

    def set_master_volume(self, volume):
        self.master_volume = volume

    def get_music_volume(self):
        return self.music_volume

    def get_sfx_volume(self):
        return self.sfx_volume

    def get_voiceover_volume(self):
        return self.voiceover_volume

    def get_master_volume(self):
        return self.master_volume

# Initialize sound options
gameSoundOptions = SoundOptions()