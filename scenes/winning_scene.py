import pygame
import game_objects
from menu.winning import Winning


class WinningScene:
    def __init__(self):
        pygame.mixer.music.load('audio/victory.wav')
        pygame.mixer.music.play(0)

    def setup(self):
        winning_scene = Winning(400, 300)
        game_objects.add(winning_scene)

    def destroy(self):
        game_objects.clear()