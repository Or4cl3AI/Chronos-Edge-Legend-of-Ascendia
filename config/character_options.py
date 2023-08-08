# This is the configuration file for character options in the game

class CharacterOptions:
    def __init__(self):
        # Character attributes
        self.max_health = 100
        self.max_stamina = 100
        self.base_attack = 10
        self.base_defense = 10
        self.base_speed = 10

        # Time manipulation abilities
        self.time_manipulation_ability = False
        self.time_manipulation_power = 0

        # Combat skills
        self.combat_skills = {
            "melee": 0,
            "ranged": 0,
            "magic": 0
        }

        # Character's destiny
        self.destiny = "unknown"

    def set_max_health(self, health):
        self.max_health = health

    def set_max_stamina(self, stamina):
        self.max_stamina = stamina

    def set_base_attack(self, attack):
        self.base_attack = attack

    def set_base_defense(self, defense):
        self.base_defense = defense

    def set_base_speed(self, speed):
        self.base_speed = speed

    def enable_time_manipulation(self):
        self.time_manipulation_ability = True

    def set_time_manipulation_power(self, power):
        self.time_manipulation_power = power

    def set_combat_skill(self, skill, level):
        if skill in self.combat_skills:
            self.combat_skills[skill] = level

    def set_destiny(self, destiny):
        self.destiny = destiny

# Initialize character options
character_options = CharacterOptions()