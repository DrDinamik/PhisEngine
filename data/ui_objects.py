from pygame import image, transform, sprite
from numpy import array, pi, zeros, int16


class Animation:
    """Class for procedural animations(WIP)"""
    def __init__(self, f, z, r, x0: array, xd: array, step=0.1):
        self.f, self.z, self.r = f, z, r
        # Compute constants
        self.k1 = self.z / (pi * self.f)
        self.k2 = (2 * pi * self.f) ** -2
        self.k3 = self.r * self.z / (2 * pi * self.f)

        self.x_prev = x0
        self.y = x0
        self.yd = 0
        self.xd = xd

        self.step = step
        self.t = 0
        print("init")

    def update(self, x: array):
        """
        Updater
        :param x: actual pos
        :return: next pos and end statement
        """
        if sum([i ** 2 for i in self.xd - x]) ** 0.5 <= 0.1:
            print("exit")
            return tuple(self.y), True
        k2_stable = max(self.k2, 1.1 * (self.t ** 2 / 4 + self.t * self.k1 / 2))  # Guarantee stability
        self.y = self.y + self.t * self.yd  # Integrate pos by velocity
        self.yd = self.yd + self.t * (x + self.k3 * self.xd - self.y - self.k1 * self.yd) / k2_stable  # Integrate pos by acceleration
        self.t += self.step
        # print(self.y, self.yd, self.t, x, self.xd)
        return tuple(self.y), None


class HiddenGroup(sprite.Group):
    def __init__(self):
        super().__init__()
        self.on = True


class Button(sprite.Sprite):
    def __init__(self, pos: array, name, construction_data, data, groups: dict, switch=False):
        super().__init__(i[1] for i in filter(lambda x: x[0] in construction_data["groups"], groups.items()))

        self.pos = pos
        self.c_data = construction_data
        self.name = name
        self.data = data

        self.switch = switch
        self.pressed = False

        self.rect = None
        self.image = None
        self.switch_img()

    def move(self, pos, scale=1., to_center=False):
        point = pos * array(self.data.scale) * scale + (array(self.data.size) / 2) if to_center else zeros(2)
        # print(self.name, pos, point)
        self.rect = self.image.get_rect().move([int16(i) for i in point])

    def resize(self):
        self.image = transform.scale(self.image, (int(self.c_data["size"][0] * self.data.scale[0]),
                                                  int(self.c_data["size"][1] * self.data.scale[1])))
        self.move(self.pos)

    def switch_img(self):
        self.image = image.load(self.c_data["img"][int(self.pressed)]).convert_alpha()
        self.resize()

    def touch(self):
        self.pressed = not self.pressed
        self.switch_img()
