import game_objects
from menu.winning import Winning

class WinningScene:
    def __init__(self):
        pass

    def setup(self):
        winning_scene = Winning(400, 300)
        game_objects.add(winning_scene)

    def destroy(self):
        game_objects.clear()