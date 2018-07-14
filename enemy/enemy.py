from game_objects import GameObject, game_objects
from map_title.wall import Wall
from physics.box_collider import BoxCollider
from frame_counter import FrameCounter
from player.player import Player
from game_objects import collide_with, add as add_game_object
from player.player_captured import PlayerCaptured
from renderer.animation import Animation
from enemy.enemy_animator import EnemyAnimator
from renderer.image_renderer import ImageRenderer
from random import choice
from scenes.scene_manager import global_scene_manager
from scenes.gameover_scene import GameOverScene


class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(32, 32)
        self.renderer = EnemyAnimator()
        self.direct = True
        self.frame_counter = FrameCounter(120)
        self.black_screen = False
        self.counter = FrameCounter(120)
        self.dy = 8
        self.dx = 0
        self.overlap = False
        self.directory = [1, 2, 3, 4]
        self.step = 8

    def update(self):
        GameObject.update(self)
        self.update_animator()
        self.frame_counter.run()
        if self.frame_counter.expired:
            self.black_screen = True
            self.counter.run()
            if self.counter.expired:
                self.black_screen = False
                self.counter.reset()
                self.frame_counter.reset()
        if not self.black_screen:
            self.move()
        else:
            pass

        collide_list = collide_with(self.box_collider, Player)
        for game_object in collide_list:
            game_object.deactivate()
            game_over = GameOverScene()
            global_scene_manager.change_scene(game_over)

    def move(self):
        if self.x > 768:
            self.dx = -self.step
            self.dy = 0
        elif self.x < 32:
            self.dx = self.step
            self.dy = 0
        elif self.y > 608:
            self.dy = -self.step
            self.dx = 0
        elif self.y < 32:
            self.dy = self.step
            self.dx = 0
        else:
            self.check_overlap()

            if not self.overlap:
                self.directory = [1, 2, 3, 4]
            else:
                if len(self.directory) == 0:
                    self.directory = [1, 2, 3, 4]

                move = choice(self.directory)

                if move == 1:
                    self.dy = self.step
                    self.dx = 0

                elif move == 2:
                    self.dy = -self.step
                    self.dx = 0

                elif move == 3:
                    self.dx = self.step
                    self.dy = 0

                elif move == 4:
                    self.dx = -self.step
                    self.dy = 0

                self.reset_boxcollider()
                self.check_overlap()
                if self.overlap:
                    self.directory.remove(move)

        self.x += self.dx
        self.y += self.dy
        self.overlap = False

    def update_animator(self):
            self.renderer.update(self.dx, self.dy)

    def check_overlap(self):
        self.box_collider.y = self.y + self.dy
        self.box_collider.x = self.x + self.dx
        for game_object in game_objects:
            if type(game_object) == Wall:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    self.overlap = True

    def reset_boxcollider(self):
        self.box_collider.x = self.x
        self.box_collider.y = self.y

