```python
import pybullet as p
from config.physics_options import PhysicsOptions

class PhysicsEngine:
    def __init__(self):
        self.physicsClient = p.connect(p.DIRECT)
        p.setGravity(0, 0, -9.8, physicsClientId=self.physicsClient)
        self.physicsOptions = PhysicsOptions()

    def update_physics(self, gameState):
        p.stepSimulation(physicsClientId=self.physicsClient)
        self.check_collisions(gameState)

    def check_collisions(self, gameState):
        for objA, objB in p.getOverlappingPairs(physicsClientId=self.physicsClient):
            self.handle_collision(objA, objB, gameState)

    def handle_collision(self, objA, objB, gameState):
        if gameState['playerCharacter']['id'] in [objA, objB]:
            self.player_collision(objA, objB, gameState)

    def player_collision(self, objA, objB, gameState):
        if gameState['playerCharacter']['id'] == objA:
            colliding_obj = objB
        else:
            colliding_obj = objA

        if colliding_obj in gameState['currentLevel']['obstacles']:
            self.player_obstacle_collision(gameState)
        elif colliding_obj in gameState['currentLevel']['enemies']:
            self.player_enemy_collision(gameState)

    def player_obstacle_collision(self, gameState):
        gameState['playerCharacter']['health'] -= self.physicsOptions.obstacle_damage
        if gameState['playerCharacter']['health'] <= 0:
            gameState['gameState'] = 'GAME_OVER'

    def player_enemy_collision(self, gameState):
        gameState['playerCharacter']['health'] -= self.physicsOptions.enemy_damage
        if gameState['playerCharacter']['health'] <= 0:
            gameState['gameState'] = 'GAME_OVER'

    def apply_force(self, obj_id, force):
        p.applyExternalForce(obj_id, -1, force, [0, 0, 0], p.LINK_FRAME, physicsClientId=self.physicsClient)

    def apply_torque(self, obj_id, torque):
        p.applyExternalTorque(obj_id, -1, torque, p.LINK_FRAME, physicsClientId=self.physicsClient)
```