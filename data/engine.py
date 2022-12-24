from numpy import array, float64, isnan, nan_to_num, hstack, ones, zeros, mean, hstack


def modulus(n: array):
    # print("Modulus:", n, array([i ** 2 for i in n]) ** 0.5 / 0)
    return sum(list(array([i ** 2 for i in n]))) ** 0.5


def distance(obj1, obj2):
    """Calculate the distance between two objects"""
    return ((obj1.pos - obj2.pos) ** 2).sum() ** 0.5


class Engine:
    def __init__(self, data):
        self.data = data
        self.objects = self.load_objects()

        self.G = 6.67408e-11  # Gravitational constant
        self.softening = 0.1  # precision metric

        self.mass = ones((len(self.objects), 1))
        self.pos = zeros((len(self.objects), 3))
        self.vel = zeros((len(self.objects), 3))

        for i, obj in enumerate(self.objects):
            self.mass[i] = obj.mass
            self.pos[i] = obj.pos
            self.vel[i] = obj.velocity

        self.vel -= mean(self.mass * self.vel, 0) / mean(self.mass)

        # calculate initial gravitational accelerations
        self.acc = self.getAcc(self.pos, self.mass, self.softening)

    def load_objects(self):
        return [MassObject(name, item["radius"], item["mass"], array(item["velocity"]), array(item["pos"]), self.data.simulation_time)
                for name, item in self.data.objects.items()]

    def interactions(self):
        """ N-body simulation """

        dt = self.data.simulation_time   # timestep

        # (1/2) kick
        self.vel += self.acc * dt/2.0

        # drift
        self.pos += self.vel * dt

        # update accelerations
        self.acc = self.getAcc(self.pos, self.mass, self.softening)

        # (1/2) kick
        self.vel += self.acc * dt/2.0

        for i, obj in enumerate(self.objects):
            obj.pos = self.pos[i]
            obj.velocity = self.vel[i]

    def getAcc(self, pos, mass, softening):
        """
        Calculate the acceleration on each particle due to Newton's Law
        pos  is an N x 3 matrix of positions
        mass is an N x 1 vector of masses
        G is Newton's Gravitational constant
        softening is the softening length
        a is N x 3 matrix of accelerations
        """
        # positions r = [x,y,z] for all particles
        x = pos[:, 0:1]
        y = pos[:, 1:2]
        z = pos[:, 2:3]

        # matrix that stores all pairwise particle separations: r_j - r_i
        dx = x.T - x
        dy = y.T - y
        dz = z.T - z

        # matrix that stores 1/r^3 for all particle pairwise particle separations
        inv_r3 = (dx ** 2 + dy ** 2 + dz ** 2 + softening ** 2)
        inv_r3[inv_r3 > 0] = inv_r3[inv_r3 > 0]**(-1.5)

        ax = self.G * (dx * inv_r3) @ mass
        ay = self.G * (dy * inv_r3) @ mass
        az = self.G * (dz * inv_r3) @ mass

        # pack together the acceleration components
        a = hstack((ax, ay, az))

        return a

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
    def __init__(self, name, radius, mass, velocity: array, pos: array, t):
        """
        Phis object in space
        :param name: name of object
        :param radius: graphical and phis interactive parameter in m
        :param mass: mass of object in kg
        :param velocity: speed of object in m/s
        :param pos: position of object in m
        :param t: simulated time in s per update (less time -> more precision and CPU load)
        """
        self.name = name
        self.radius = radius
        self.mass = mass
        self.velocity = velocity
        self.pos = pos
        self.time = t

    def update(self):
        # print(self.name, self.pos, self.velocity)
        self.pos += self.velocity * self.time


if __name__ == "__main__":
    print("Holy shi...")
