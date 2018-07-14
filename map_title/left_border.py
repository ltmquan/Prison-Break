from game_objects import GameObject
from renderer.image_renderer import ImageRenderer


class LeftBorder(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("image/map/image/4.png")