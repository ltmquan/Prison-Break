class SceneManager:
    def __init__(self):
        self.current_scene = None

    def change_scene(self, new_scene):
        if self.current_scene is not None:
            self.current_scene.destroy()
        new_scene.setup()
        self.current_scene = new_scene

global_scene_manager = SceneManager()
