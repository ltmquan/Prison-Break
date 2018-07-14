from renderer.image_renderer import ImageRenderer
from game_objects import GameObject
# from input.input_manager import global_input_manager
# from scenes.scene_manager import global_scene_manager
# from scenes.gameplay_scene import GameplayScene

class GameOver(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("image/menu/Gameover.png")

    # def update(self):
    #     if global_input_manager.enter_pressed:
    #         gameplay_scene = GameplayScene()
    #         global_scene_manager.change_scene(gameplay_scene)