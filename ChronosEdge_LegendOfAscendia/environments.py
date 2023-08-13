```python
import UnrealEngine5 as ue5
import HavokPhysics as hp

class Environment:
    def __init__(self, name, description, is_dangerous):
        self.name = name
        self.description = description
        self.is_dangerous = is_dangerous
        self.visuals = None
        self.physics = None

    def generate_visuals(self):
        self.visuals = ue5.render(self.name)

    def apply_physics(self):
        self.physics = hp.apply(self.name)

    def is_safe(self):
        return not self.is_dangerous

class AncientRuins(Environment):
    def __init__(self):
        super().__init__("Ancient Ruins", "Breathtaking vistas of ancient ruins", True)

class FuturisticCity(Environment):
    def __init__(self):
        super().__init__("Futuristic City", "Towering spires of futuristic cities", False)

def create_environments():
    environments = [AncientRuins(), FuturisticCity()]
    for environment in environments:
        environment.generate_visuals()
        environment.apply_physics()
    return environments
```