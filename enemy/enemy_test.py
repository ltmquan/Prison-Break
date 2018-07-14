from game_objects import GameObject
from physics.box_collider import BoxCollider
from player.player import Player
from input.input_manager import InputManager
from game_objects import collide_with, add as add_game_object
# from player.player_captured import PlayerCaptured
# from renderer.animation import Animation
input_manager = InputManager()
player = Player(16, 16, input_manager)


class Enemy(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(32, 32)
        self.input_manager = input_manager
        # self.renderer = Animation([])

    def update(self):
        GameObject.update(self)
        self.move()

        # collide_list = collide_with(self.box_collider, Player)
        # for game_object in collide_list:
        #     capture = PlayerCaptured(game_object.x, game_object.y)
        #     add_game_object(capture)
        #     game_object.deactivate()
        #     self.deactivate()

    def move(self):
        if self.input_manager.KEYDOWN:
            if self.x > player.x:
                if self.y == player.y:
                    self.x -= 32
                    self.x -= 32
                elif self.y < player.y:
                    self.y += 32
                    self.x -= 32
                elif self.y > player.y:
                    self.y -= 32
                    self.x -= 32
            elif self.x < player.x:
                if self.y == player.y:
                    self.x += 32
                    self.x += 32
                elif self.y < player.y:
                    self.y += 32
                    self.x += 32
                elif self.y > player.y:
                    self.y -= 32
                    self.x += 32
            elif self.x == self.y:
                if self.y < player.y:
                    self.y += 64
                elif self.y > player.y:
                    self.y -= 64
            self.input_manager.KEYDOWN = False

