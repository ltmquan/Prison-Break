from renderer.animation import Animation
from renderer.image_renderer import ImageRenderer


class PlayerEnemyAnimator:
    def __init__(self):
        self.right_animation = Animation(["image/nigga ++/nigga ++ right/nnigga10.png",
                                          "image/nigga ++/nigga ++ right/nnigga12.png",
                                          "image/nigga ++/nigga ++ right/nnigga14.png",
                                          "image/nigga ++/nigga ++ right/nnigga16.png",
                                          "image/nigga ++/nigga ++ right/nnigga18.png"],
                                         loop=True)
        self.left_animation = Animation(["image/nigga ++/nigga ++ lefy/nnigga10.png",
                                         "image/nigga ++/nigga ++ lefy/nnigga12.png",
                                         "image/nigga ++/nigga ++ lefy/nnigga14.png",
                                         "image/nigga ++/nigga ++ lefy/nnigga16.png",
                                         "image/nigga ++/nigga ++ lefy/nnigga18.png"],
                                        loop=True)
        self.up_animation = Animation(["image/nigga ++/nigga ++ up/nnigga10.png",
                                       "image/nigga ++/nigga ++ up/nnigga12.png",
                                       "image/nigga ++/nigga ++ up/nnigga14.png",
                                       "image/nigga ++/nigga ++ up/nnigga16.png",
                                       "image/nigga ++/nigga ++ up/nnigga18.png"],
                                      loop=True)
        self.down_animation = Animation(["image/nigga ++/nigga ++ down/nnigga10.png",
                                         "image/nigga ++/nigga ++ down/nnigga12.png",
                                         "image/nigga ++/nigga ++ down/nnigga14.png",
                                         "image/nigga ++/nigga ++ down/nnigga16.png",
                                         "image/nigga ++/nigga ++ down/nnigga18.png"],
                                        loop=True)
        self.right_stand = ImageRenderer("image/nigga ++/nigga ++ right/nnigga10.png",)
        self.left_stand = ImageRenderer("image/nigga ++/nigga ++ lefy/nnigga10.png",)
        self.down_stand = ImageRenderer("image/nigga ++/nigga ++ down/nnigga10.png",)
        self.up_stand = ImageRenderer("image/nigga ++/nigga ++ up/nnigga10.png",)
        self.current_animation = self.left_stand

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