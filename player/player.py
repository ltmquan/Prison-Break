import pygame
from game_objects import GameObject, game_objects
from frame_counter import FrameCounter
from map_title.wall import Wall
from physics.box_collider import BoxCollider
from game_objects import collide_with, add as add_game_object
# from victory.player_escaped import PlayerEscaped
from player.player_animator import PlayerAnimator
# from black_slave.prison_break import PrisonBreak
from input.input_manager import global_input_manager
from player.player_enemy_animator import PlayerEnemyAnimator


class Player(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(32, 32)
        self.renderer_saved = PlayerEnemyAnimator()
        self.renderer = PlayerAnimator()
        self.frame_counter = FrameCounter(120)
        self.counter = FrameCounter(120)
        self.black_screen = False
        self.dx = 0
        self.dy = 0
        self.win = False
        self.step = 8
        self.overlap = False
        self.direct = 1

    def check_overlap(self):
        for game_object in game_objects:
            if type(game_object) == Wall:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    self.overlap = True

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
        if self.black_screen:
            self.move()
        else:
            self.dy = 0
            self.dx = 0

        # collide_list = collide_with(self.box_collider, BlackSlave)
        # for game_object in collide_list:
        #     game_object.deactivate()
        #     self.win = True

    # if self.win:
    #     collide_list1 = collide_with(self.box_collider, MainDoor)
    #     for game_object in collide_list1:
    #         # self.deactivate()
    #         pass
    #     print("aaaa")

    def update_animator(self):
        self.renderer.update(self.dx, self.dy, self.direct)

    def move(self):
        self.dx = 0
        self.dy = 0
        # self.check_collision()
        if self.x == 768:
            global_input_manager.right_pressed = False
        if self.x == 32:
            global_input_manager.left_pressed = False
        if self.y == 576:
            global_input_manager.down_pressed = False
        if self.y == 32:
            global_input_manager.up_pressed = False

        if global_input_manager.right_pressed:
            self.direct = 1
            self.box_collider.x = self.x + self.step
            self.check_overlap()
            if self.overlap:
                self.dx += 0
            else:
                self.dx += self.step

        elif global_input_manager.left_pressed:
            self.direct = 2
            self.box_collider.x = self.x - self.step
            self.check_overlap()
            if self.overlap:
                self.dx += 0
            else:
                self.dx -= self.step

        elif global_input_manager.down_pressed:
            self.direct = 4
            self.box_collider.y = self.y + self.step
            self.check_overlap()
            if self.overlap:
                self.dy += 0
            else:
                self.dy += self.step

        elif global_input_manager.up_pressed:
            self.direct = 3
            self.box_collider.y = self.y - self.step
            self.check_overlap()
            if self.overlap:
                self.dy += 0
            else:
                self.dy -= self.step

        self.x += self.dx
        self.y += self.dy
        self.box_collider.x = self.x
        self.box_collider.y = self.y
        self.overlap = False

    # def check_collision(self):
    #
    #     collide_list = collide_with(self.box_collider, Wall)
    #     for game_object in collide_list:
    #         if self.x + self.dx + 32 == game_object.x:
    #             self.input_manager.right_pressed = False
    #         elif self.x + self.dx - 32 == game_object.x:
    #             self.input_manager.left_pressed = False
    #         elif self.y + self.dy + 32 == game_object.y:
    #             self.input_manager.down_pressed = False
    #         elif self.y + self.dy - 32 == game_object.y:
    #             self.input_manager.up_pressed = False
        # if len(collide_list) > 0:
        #     self.dx = 0
        #     self.dy = 0
        # last_direct = ()
        # collide_list = collide_with(self.box_collider, Wall)
        # if self.dx < 0:






