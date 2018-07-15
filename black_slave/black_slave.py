from game_objects import GameObject
from player.player_animator import PlayerAnimator
from renderer.animation import Animation
from physics.box_collider import BoxCollider
from game_objects import collide_with, add as add_game_object
from player.player import Player
# from black_slave.rescue import Rescue
from renderer.image_renderer import ImageRenderer


class BlackSlave(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("image/slave/prisoner.png")
        self.box_collider = BoxCollider(32, 32)

    def update(self):
        GameObject.update(self)

        collide_list = collide_with(self.box_collider, Player)
        for game_object in collide_list:
            # rescue = Rescue(game_object.x, game_object.y)
            # add_game_object(rescue)
            self.deactivate()
            game_object.win = True
            game_object.renderer = PlayerAnimator(True)
