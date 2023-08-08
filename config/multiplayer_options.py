# Multiplayer options configuration

class MultiplayerOptions:
    def __init__(self):
        self.cooperative_missions_enabled = True
        self.pvp_arenas_enabled = True
        self.max_players_in_coop = 4
        self.max_players_in_pvp = 8
        self.voice_chat_enabled = True
        self.matchmaking_enabled = True
        self.friend_invite_enabled = True

    def toggle_cooperative_missions(self):
        self.cooperative_missions_enabled = not self.cooperative_missions_enabled

    def toggle_pvp_arenas(self):
        self.pvp_arenas_enabled = not self.pvp_arenas_enabled

    def set_max_players_in_coop(self, max_players):
        self.max_players_in_coop = max_players

    def set_max_players_in_pvp(self, max_players):
        self.max_players_in_pvp = max_players

    def toggle_voice_chat(self):
        self.voice_chat_enabled = not self.voice_chat_enabled

    def toggle_matchmaking(self):
        self.matchmaking_enabled = not self.matchmaking_enabled

    def toggle_friend_invite(self):
        self.friend_invite_enabled = not self.friend_invite_enabled


# Initialize multiplayer options
multiplayer_options = MultiplayerOptions()