import pygame
import game_objects
from menu.menu import Menu

class MenuScene:
    def __init__(self):
        pygame.mixer.music.load('audio/xoso.wav')
        pygame.mixer.music.play(0)

    def setup(self):
        menu = Menu(400, 300)
        game_objects.add(menu)

    def destroy(self):
        game_objects.clear()