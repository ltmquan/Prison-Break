import pygame
from game_objects import GameObject
from physics.box_collider import BoxCollider
from frame_counter import FrameCounter


class BlackScreen(GameObject):
    def __init__(self, x=0, y=0):
        GameObject.__init__(self, x, y)
        self.counter = FrameCounter(120)
        self.frame_counter = FrameCounter(120)
        self.screen = True
        self.box_collider = BoxCollider(800, 640)

    def update(self):
        GameObject.update(self)
        self.counter.run()
        if self.counter.expired:
            self.frame_counter.run()
            self.screen = False
            if self.frame_counter.expired:
                self.screen = True
                self.counter.reset()
                self.frame_counter.reset()

    def render(self, canvas):
        if not self.screen:
            BLACK = (0, 0, 0)
            rect = (0, 0, 800, 640)
            pygame.draw.rect(canvas, BLACK, rect, 1)
            canvas.fill(BLACK)

