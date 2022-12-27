from math import *
import time as time
import matplotlib.pyplot as plt
import numpy as np

U = 1170
m0 = 46797
k = 244
G = 6.67 * 10**(-11)
M = 5.2915158 * 10**22
R = 600000

def h(t):
    return -(G*M + R**2*U) * ((k*t - m0) * log(1 - k*t/m0) - k*t) / k / R**2

def v(t):
    return -U*log((m0-k*t)/m0)-(G*M/(R+h(t))**2)*log((m0-k*t)/m0)

def m(t):
    return m0-k*t


t = np.array([t for t in range(0, 61)])
vv = np.array([v(t) for t in range(0, 61)])
hh = np.array([h(t) for t in range(0, 61)])
mm = np.array([m(t) for t in range (0, 61)])

height = plt.subplot(2, 2, 1)
plt.xlabel("Время")
plt.ylabel("Высота корабля над уровнем моря")
height.plot(t, hh)
plt.grid()

velocity = plt.subplot(2, 2, 2)
plt.xlabel("Время")
plt.ylabel("Вертикальная скорость взлета")
velocity.plot(t, vv)
plt.grid()

mass = plt.subplot(3, 1, 3)
plt.xlabel("Время")
plt.ylabel("Масса корабля")
mass.plot(t, mm)
plt.grid()

plt.show()
