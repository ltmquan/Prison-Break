from player.player import Player
from enemy.enemy import Enemy
from black_slave.black_slave import BlackSlave
from victory.main_door import MainDoor
from black_screen import BlackScreen
from maps.map_gen import *
import game_objects

class GameplayScene:
    def __init__(self):
        pass
    def setup(self):

        generate_map("image/map/map.json")

        enemy = Enemy(368, 608)
        game_objects.add(enemy)

        enemy1 = Enemy(640, 300)
        game_objects.add(enemy1)

        main_door = MainDoor(16, 320)
        game_objects.add(main_door)

        black_screen = BlackScreen(0, 0)
        game_objects.add(black_screen)

        player = Player(64, 320)
        game_objects.add(player)

        black_slave = BlackSlave(768, 580)
        game_objects.add(black_slave)

    def destroy(self):
        game_objects.clear()