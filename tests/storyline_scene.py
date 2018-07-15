import pygame
from input.input_manager import InputManager
from player.player import Player
from frame_counter import FrameCounter
import game_objects
from enemy.enemy import Enemy
# from maze.bricks import Brick
from black_screen import BlackScreen
from black_slave.black_slave import BlackSlave
from victory.main_door import MainDoor
from maps.map_gen import *
from tests.storyline import storyline


BG = (255, 255, 0)
WHITE = (255, 255, 255)

# 1. Init pygame
pygame.init()

# 2. Set screen
SIZE = (780, 620)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

loop = True

input_manager = InputManager()

while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    game_objects.update()

    # 2. Draw
    canvas.fill(WHITE)

    game_objects.render(canvas)

    pygame.display.set_caption('Micro game')

    # 3. Flip
    pygame.display.flip()
    clock.tick(60)