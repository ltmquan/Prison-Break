import pygame
from frame_counter import FrameCounter


class Animation:
    def __init__(self, image_urls, loop=False, frame_delay=5):
        self.images = [pygame.image.load(image_url) for image_url in image_urls]
        self.image_index = 0
        self.finished = False
        self.frame_counter = FrameCounter(frame_delay)
        self.loop = loop

    def render(self, canvas, x, y):
        if not self.finished or self.loop:
            current_image = self.images[self.image_index]
            width = current_image.get_width()
            height = current_image.get_height()
            render_pos = (x - width / 2, y - height / 2)
            canvas.blit(current_image, render_pos)
        self.frame_counter.run()
        if self.frame_counter.expired:
            self.frame_counter.reset()
            if self.image_index < len(self.images) - 1:
                self.image_index += 1
            elif self.loop:
                self.image_index = 0
            else:
                self.finished = True