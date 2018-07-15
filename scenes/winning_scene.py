import pygame
import game_objects
from menu.winning import Winning
from renderer.image_renderer import ImageRenderer


class WinningScene:
    def __init__(self):
        self.renderer = ImageRenderer("image/37206651_226948211286290_1494096384997982208_n.png")
        pygame.mixer.music.load("audio/victory.wav")
        pygame.mixer.music.play(0)

    def setup(self):
        winning_scene = Winning(400, 300)
        game_objects.add(winning_scene)

    def destroy(self):
        game_objects.clear()