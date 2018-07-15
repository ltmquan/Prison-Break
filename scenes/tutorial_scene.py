import pygame
import game_objects
from menu.tutorial import Tutorial


class TutorialScene:
    def __init__(self):
        pass

    def setup(self):
        tutorial = Tutorial(400, 300)
        game_objects.add(tutorial)

    def destroy(self):
        game_objects.clear()