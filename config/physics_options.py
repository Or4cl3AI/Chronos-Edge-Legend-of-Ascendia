# config/physics_options.py

```python
class PhysicsOptions:
    def __init__(self):
        self.gravity = -9.8  # Gravity value
        self.air_resistance = 0.1  # Air resistance value
        self.friction = 0.5  # Friction value
        self.time_dilation = 1.0  # Time dilation value for time manipulation

    def set_gravity(self, value):
        self.gravity = value

    def set_air_resistance(self, value):
        self.air_resistance = value

    def set_friction(self, value):
        self.friction = value

    def set_time_dilation(self, value):
        self.time_dilation = value

physics_options = PhysicsOptions()
```