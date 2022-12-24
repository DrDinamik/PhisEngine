<<<<<<< HEAD
from pygame import display, RESIZABLE, init, event
from time import perf_counter
from data.ui_objects import *
from data.events import Events
from numpy import array


class InterfaceHandler:
    def __init__(self, data, engine):
        init()
        self.data = data
        self.eng = engine
        self.events = Events(self.data)

        self.screen = display.set_mode(self.data.size, RESIZABLE)
        display.set_caption(self.data.settings["title"])
        self.sprites = {}
        self.groups = {item: HiddenGroup() for item in data.ui_objects["groups"]}
        self.load_placements()

        self.center = self.center = array([0, 0, 0])
        self.counter = perf_counter
        self.prev_update = self.counter()

    def load_placements(self):
        for item in self.data.ui_objects["placements"]:
            if item["type"] == "button":
                group = self.data.ui_objects["types"][item["type"]]["groups"] + item["groups"] if item.get("groups") else []
                cd = self.data.ui_objects["types"][item["type"]]
                cd["groups"] = group
                self.sprites[item["name"]] = Button(pos=array(item["pos"]),
                                                    name=item["name"],
                                                    construction_data=cd,
                                                    data=self.data,
                                                    groups=self.groups,
                                                    switch=item["switch"] if item.get("switch") else False)

    def to_plane(self, pos: array):
        return pos * self.data.settings["plane_scale"] + self.center + array(list(array(self.data.size) / 2) + [0])

    def update(self):
        if self.counter() - self.prev_update >= self.data.settings["fps"] ** -1:

            self.events.update(event.get())
            self.screen = display.set_mode(self.data.size, RESIZABLE)
            # print([item.pos for item in self.eng.objects])

            self.screen.fill((255, 255, 255))

            for obj in self.eng.objects:
                for name, spr in self.sprites.items():
                    if obj.name == name:
                        self.sprites[name].move(obj.pos[:2], scale=self.data.dyn_scale, to_center=True)

            for name, item in self.groups.items():
                if item.on:
                    item.draw(self.screen)

            self.prev_update = self.counter()
            display.flip()


if __name__ == "__main__":
    print("Why are you running?")
=======
from pygame import image, transform, sprite, display, RESIZABLE, init
from time import perf_counter
from numpy import array


class InterfaceHandler:
    def __init__(self, data, engine):
        init()
        self.data = data
        self.eng = engine

        self.screen = display.set_mode(data.window_size, RESIZABLE)
        self.sprites = []
        self.groups = {item: HiddenGroup() for item in data.ui_objects["groups"]}
        self.load_placements()

        self.counter = perf_counter
        self.prev_update = self.counter()

    def load_placements(self):
        for item in self.data.ui_objects["placements"]:
            if item["type"] == "button":
                self.sprites += [Button(array(item["pos"]), item["name"], self.data.ui_objects["types"][item["type"]], self.data, self.groups, switch=item["switch"] if item.get("switch") else False)]

    def update(self):
        if self.counter() - self.prev_update >= self.data.settings["fps"] ** -1:
            print(self.counter())
            self.prev_update = self.counter()
            for name, item in self.groups.items():
                if item.on:
                    item.draw(self.screen)
            display.flip()


class HiddenGroup(sprite.Group):
    def __init__(self):
        super().__init__()
        self.on = True


class Button(sprite.Sprite):
    def __init__(self, pos: array, button_name, construction_data, dc, groups: dict, switch=False):
        super().__init__(i[1] for i in filter(lambda x: x[0] in construction_data["groups"], groups.items()))

        self.pos = pos
        self.data = construction_data
        self.name = button_name
        self.dc = dc

        self.image = image.load(self.data["img"][0]).convert_alpha()
        self.rect = 0
        self.resize()

        self.is_switch = switch
        self.is_pressed = False

    def move(self, pos):
        self.rect = self.image.get_rect().move(list(pos * array(self.dc.scale)))

    def resize(self):
        self.image = transform.scale(self.image, (int(self.data["size"][0] * self.dc.scale[0]),
                                                  int(self.data["size"][1] * self.dc.scale[1])))
        self.move(self.pos)

    def switch_img(self):
        self.image = image.load(self.data["img"][int(self.is_pressed)]).convert_alpha()
        self.resize()

    def touch(self):
        self.is_pressed = not self.is_pressed
        self.switch_img()


if __name__ == "__main__":
    print("Why are you running?")
>>>>>>> origin/main
