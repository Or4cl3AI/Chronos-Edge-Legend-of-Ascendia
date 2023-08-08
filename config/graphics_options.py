```python
class GraphicsOptions:
    def __init__(self):
        self.resolution = (1920, 1080)
        self.fullscreen = True
        self.vsync = True
        self.texture_quality = 'High'
        self.shadow_quality = 'High'
        self.anti_aliasing = 'High'
        self.view_distance = 'Far'
        self.fps_limit = 60

    def set_resolution(self, width, height):
        self.resolution = (width, height)

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen

    def toggle_vsync(self):
        self.vsync = not self.vsync

    def set_texture_quality(self, quality):
        self.texture_quality = quality

    def set_shadow_quality(self, quality):
        self.shadow_quality = quality

    def set_anti_aliasing(self, quality):
        self.anti_aliasing = quality

    def set_view_distance(self, distance):
        self.view_distance = distance

    def set_fps_limit(self, limit):
        self.fps_limit = limit

gameSettings = GraphicsOptions()
```