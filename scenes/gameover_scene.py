import game_objects
from menu.gameover import GameOver

class GameOverScene:
    def __init__(self):
        pass

    def setup(self):
        game_over_scene = GameOver(400, 300)
        game_objects.add(game_over_scene)

    def destroy(self):
        game_objects.clear()