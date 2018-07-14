from renderer.image_renderer import ImageRenderer
from game_objects import GameObject

class Winning(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("image/menu/winning_scene.png")

