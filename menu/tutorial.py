from game_objects import GameObject
from renderer.animation import Animation
from input.input_manager import global_input_manager
from scenes.scene_manager import global_scene_manager
# from scenes.guide_scene import GuideScene
from scenes.gameplay_scene import GameplayScene
from renderer.image_renderer import ImageRenderer


class Tutorial(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("image/37059021_226940234620421_6512011225008701440_n.png")

    def update(self):
        if global_input_manager.enter_pressed:
            gameplay_scene = GameplayScene()
            global_scene_manager.change_scene(gameplay_scene)