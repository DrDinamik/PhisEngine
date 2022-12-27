from math import *
import time as time
import matplotlib.pyplot as plt
import numpy as np

G = 6.67 * 10**(-11)
vn = 3018.474
vp = 7581.594
tetta = 0
R = 1.35994977 * 10**10
M = 1.7565459 * 10**28
r = R
m = 3500
L = m*r*vp
eps = 0.59755027622
K = (G*M*m)
tetta0 = 1.9605368840507695
PI = acos(-1)


def dist(tetta):
    return (L**2/(K*m)) * (1/(1+eps*cos(tetta - tetta0)))

def velocity(tetta):
    return (vn + (eps*sin(tetta-tetta0)/(eps*cos(tetta-tetta0)+1)**2))

def w(v, r):
    return v/r

ang = np.array([])

while tetta < 2*PI:
    ang = np.append(ang, tetta)
    tetta += 0.01


vv = np.array([velocity(tetta) for tetta in ang])
hh = np.array([dist(tetta) for tetta in ang])
ww = np.array([])

for i in range(len(vv)):
    ww  = np.append(ww, w(vv[i], hh[i]))


degrees = np.array([180 * x / PI for x in ang])


height = plt.subplot(2, 2, 1)
height.set(xlim=(0, 360))
plt.xlabel("Полярный угол θ")
plt.ylabel("Расстояние до Кербола")
height.plot(degrees, hh)
plt.grid()

velocity = plt.subplot(2, 2, 2)
velocity.set(xlim=(0, 360))
plt.xlabel("Полярный угол θ")
plt.ylabel("Скорость по направлению к Керболу")
velocity.plot(degrees, vv)
plt.grid()

aw = plt.subplot(3, 1, 3)
aw.set(xlim=(0, 360))
plt.xlabel("Полярный угол θ")
plt.ylabel("Угловая скорость")
aw.plot(degrees, ww)
plt.grid()

plt.show()