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
