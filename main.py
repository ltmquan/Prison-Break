import pygame
from input.input_manager import global_input_manager
# from player.player import Player
# from frame_counter import FrameCounter
# import game_objects
# from enemy.enemy import Enemy
# from maze.bricks import Brick
# from black_screen import BlackScreen
# from black_slave.black_slave import BlackSlave
# from victory.main_door import MainDoor
from maps.map_gen import *
from scenes.menu_scene import MenuScene
from scenes.scene_manager import global_scene_manager
# from scenes.guide_scene import GuideScene
from scenes.gameplay_scene import GameplayScene

BG = (255, 255, 0)
WHITE = (255, 255, 255)

# 1. Init pygame
pygame.init()

# 2. Set screen
SIZE = (800, 620)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

loop = True

generate_map("image/map/map.json")

menu_scene = MenuScene()
global_scene_manager.change_scene(menu_scene)

# guide_scene = GuideScene()
# global_scene_manager.change_scene(guide_scene)
# player = Player(32, 320, input_manager)
# enemy = Enemy(368, 608)
# enemy1 = Enemy(640, 300)
#
# black_slave = BlackSlave(768, 240)
# black_screen = BlackScreen(0, 0)
# main_door = MainDoor(16, 320)
#
# game_objects.add(enemy)
# game_objects.add(black_slave)
# game_objects.add(main_door)
# game_objects.add(enemy1)
# game_objects.add(black_screen)
# game_objects.add(player)

while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            gameplay_scene = GameplayScene()
            global_scene_manager.change_scene(gameplay_scene)
        else:
            global_input_manager.update(event)

    game_objects.update()

    # 2. Draw
    canvas.fill(WHITE)

    game_objects.render(canvas)

    pygame.display.set_caption('Micro game')

    # 3. Flip
    pygame.display.flip()
    clock.tick(60)