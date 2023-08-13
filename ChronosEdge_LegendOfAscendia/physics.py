```python
import HavokPhysics

class PhysicsEngine:
    def __init__(self):
        self.engine = HavokPhysics.Engine()

    def apply_gravity(self, character):
        self.engine.apply_force(character, self.engine.GRAVITY)

    def apply_jump_force(self, character, force):
        self.engine.apply_force(character, -force)

    def apply_movement_force(self, character, direction, force):
        self.engine.apply_force(character, force * direction)

    def check_collision(self, character, environment):
        return self.engine.check_collision(character, environment)

    def handle_collision(self, character, environment):
        if self.check_collision(character, environment):
            self.engine.resolve_collision(character, environment)

    def update_character_physics(self, character):
        self.apply_gravity(character)
        character.update_position(self.engine.get_velocity(character))

    def perform_acrobatic_maneuver(self, character, maneuver):
        force, direction = maneuver.get_force_and_direction()
        self.apply_movement_force(character, direction, force)
        character.perform_maneuver(maneuver)

    def perform_strike(self, character, enemy, weapon):
        force, direction = weapon.get_force_and_direction()
        self.apply_movement_force(enemy, direction, force)
        enemy.take_damage(weapon.get_damage())

    def update(self, characters, environments):
        for character in characters:
            self.update_character_physics(character)
            for environment in environments:
                self.handle_collision(character, environment)
```
