import game_objects
import json
from addict import Dict
from map_title.down_border import DownBorder
from map_title.left_border import LeftBorder
from map_title.right_border import RightBorder
from map_title.up_border import UpBorder
from map_title.wall import Wall
from map_title.ground import Ground


def load_map(json_file_url):
    text = open(json_file_url, "r").read()

    map_dict = json.loads(text)

    map = Dict(map_dict)

    data = map.layers[0].data
    width = map.width
    height = map.height

    return data, width, height


def generate_map(json_file_url):
    data, width, height = load_map(json_file_url)

    for index, title in enumerate(data):
        title_x = index % width
        title_y= index // width
        if title == 0:
            pass
        elif title == 1:
            game_objects.add(RightBorder(title_x*32, title_y*32))
        elif title == 2:
            game_objects.add(UpBorder(title_x*32, title_y*32))
        elif title == 3:
            game_objects.add(DownBorder(title_x * 32, title_y * 32))
        elif title == 4:
            game_objects.add(LeftBorder(title_x * 32, title_y * 32))
        elif title == 5:
            game_objects.add(Ground(title_x * 32, title_y * 32))
        elif title == 6:
            game_objects.add(Wall(title_x * 32, title_y * 32))
