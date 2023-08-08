# This file contains the configuration options for the arenas in the game

class ArenaOptions:
    def __init__(self):
        # The maximum number of players in an arena
        self.max_players = 10

        # The minimum number of players in an arena
        self.min_players = 2

        # The time limit for an arena match in minutes
        self.time_limit = 15

        # The score limit for an arena match
        self.score_limit = 50

        # The respawn time for players in seconds
        self.respawn_time = 5

        # The list of available arenas
        self.available_arenas = ["Arena1", "Arena2", "Arena3", "Arena4", "Arena5"]

    def get_max_players(self):
        return self.max_players

    def get_min_players(self):
        return self.min_players

    def get_time_limit(self):
        return self.time_limit

    def get_score_limit(self):
        return self.score_limit

    def get_respawn_time(self):
        return self.respawn_time

    def get_available_arenas(self):
        return self.available_arenas
