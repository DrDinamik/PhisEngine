from typing import Callable
from numpy import array


class Engine:
    def __init__(self, t):
        self.time = t
        self.objects = []

    def interactions(self, inter_func: Callable):
        for i in range(len(self.objects)):
            for j in range(len(self.objects)):
                if i - j and self.objects[i].mass:
                    self.objects[i] = inter_func(self.objects[i], self.objects[j])

    def __iadd__(self, other):
        self.objects.append(other)
        return self

    def __add__(self, other):
        self.objects.append(other)
        return self

    def __getitem__(self, item):
        if type(item) is int:
            return self.objects[item]
        elif type(item) is str:
            for i in self.objects:
                if i.name == item:
                    return i


class MassObject:
    def __init__(self, name, radius, mass, speed: array, pos: array, t):
        """
        Phis or graphical object in space
        :param name: name of object
        :param radius: graphical and phis interactive parameter in m
        :param mass: mass of object in kg
        :param speed: speed of object in m/s
        :param pos: position of object in m
        :param t: simulated time in s per update (less time -> more precision and load)
        """
        self.name = name
        self.radius = radius
        self.mass = mass
        self.speed = speed
        self.pos = pos
        self.time = t

    def update(self):
        self.pos += self.speed * self.time


def main():
    time_per_tick = 10000
    e = Engine(1000)
    e += MassObject("camera", 0, 0, array([0.001, 0.02, -0.3]), array([0., 0., 0.]), t=time_per_tick)
    for i in range(1000):
        e["camera"].update()
        print(e["camera"].pos)


if __name__ == "__main__":
    main()
