import pygame
import game_objects
from menu.gameover import GameOver

class GameOverScene:
    def __init__(self):
        pygame.mixer.music.load('audio/game_over.flac')
        pygame.mixer.music.play(0)

    def setup(self):
        game_over_scene = GameOver(400, 300)
        game_objects.add(game_over_scene)

    def destroy(self):
        game_objects.clear()