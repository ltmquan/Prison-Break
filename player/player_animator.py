from renderer.animation import Animation
from renderer.image_renderer import ImageRenderer


class PlayerAnimator:
    def __init__(self):
            self.right_animation = Animation(["image/nigga/nigga right/nigga10.png",
                                              "image/nigga/nigga right/nigga12.png",
                                              "image/nigga/nigga right/nigga14.png",
                                              "image/nigga/nigga right/nigga16.png",
                                              "image/nigga/nigga right/nigga18.png"],
                                             loop=True)
            self.left_animation = Animation(["image/nigga/nigga left/nigga10.png",
                                             "image/nigga/nigga left/nigga12.png",
                                             "image/nigga/nigga left/nigga14.png",
                                             "image/nigga/nigga left/nigga16.png",
                                             "image/nigga/nigga left/nigga18.png"],
                                            loop=True)
            self.up_animation = Animation(["image/nigga/nigga up/nigga10.png",
                                           "image/nigga/nigga up/nigga12.png",
                                           "image/nigga/nigga up/nigga14.png",
                                           "image/nigga/nigga up/nigga16.png",
                                           "image/nigga/nigga up/nigga18.png"],
                                          loop=True)
            self.down_animation = Animation(["image/nigga/nigga down/nigga10.png",
                                             "image/nigga/nigga down/nigga12.png",
                                             "image/nigga/nigga down/nigga14.png",
                                             "image/nigga/nigga down/nigga16.png",
                                             "image/nigga/nigga down/nigga18.png"],
                                            loop=True)
            self.right_stand = ImageRenderer("image/nigga/nigga right/nigga10.png")
            self.left_stand = ImageRenderer("image/nigga/nigga left/nigga10.png")
            self.down_stand = ImageRenderer("image/nigga/nigga down/nigga10.png")
            self.up_stand = ImageRenderer("image/nigga/nigga up/nigga10.png")
            self.current_animation = self.right_stand

    def render(self, canvas, x, y):
        self.current_animation.render(canvas, x, y)

    def update(self, player_dx, player_dy, player_direct):
        if player_direct == 2:
            if player_dx < 0:
                self.current_animation = self.left_animation
            elif player_dx == 0:
                self.current_animation = self.left_stand
        if player_direct == 1:
            if player_dx > 0:
                self.current_animation = self.right_animation
            elif player_dx == 0:
                self.current_animation = self.right_stand
        if player_direct == 4:
            if player_dy > 0:
                self.current_animation = self.down_animation
            elif player_dy == 0:
                self.current_animation = self.down_stand
        if player_direct == 3:
            if player_dy < 0:
                self.current_animation = self.up_animation
            elif player_dy == 0:
                self.current_animation = self.up_stand



