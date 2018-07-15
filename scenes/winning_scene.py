import pygame
import game_objects
from menu.winning import Winning


class WinningScene:
    def __init__(self):
        pygame.mixer.music.load('image/37206651_226948211286290_1494096384997982208_n.png')
        pygame.mixer.music.play(0)

    def setup(self):
        winning_scene = Winning(400, 300)
        game_objects.add(winning_scene)

    def destroy(self):
        game_objects.clear()