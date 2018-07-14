from game_objects import GameObject
from renderer.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
# from player.player import Player
from game_objects import collide_with, add as add_game_object


class Wall(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("image/map/image/6.png")
        self.box_collider = BoxCollider(16, 16)

    def update(self):
        GameObject.update(self)



