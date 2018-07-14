game_objects = []


def add(game_object):
    game_objects.append(game_object)

def clear():
    game_objects.clear()

def update():
    for game_object in game_objects:
        if game_object.is_active:
            game_object.update()


def render(canvas):
    for game_object in game_objects:
        if game_object.is_active:
            game_object.render(canvas)


def recycle(t, x, y):
    for game_object in game_objects:
        if not game_object.is_active and type(game_object) == t:
            game_object.is_active = True
            game_object.x = x
            game_object.y = y
            return game_object

    new_game_object = t(x, y)
    add(new_game_object)
    return new_game_object


def collide_with(box_collider, wanted_type): #wanted_type để tối ưu hóa
    collide_list = []
    for game_object in game_objects:
        if game_object.is_active and game_object.box_collider is not None:
            if type(game_object) == wanted_type:
                if game_object.box_collider.overlap(box_collider):
                    collide_list.append(game_object)
    return collide_list


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_active = True
        self.renderer = None
        self.box_collider = None

    def update(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x
            self.box_collider.y = self.y

    def render(self, canvas):
        if self.renderer is not None:
            self.renderer.render(canvas, self.x, self.y)
        if self.box_collider is not None:
            self.box_collider.render(canvas)

    def deactivate(self):
        self.is_active = False