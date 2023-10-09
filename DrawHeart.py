import math
from turtle import *


def heart_a(k):
    return 15 * math.sin(k) ** 3


def heart_b(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(k * 2) - 2 * \
           math.cos(k * 3) - \
           math.cos(k * 4)


speed(6000)
bgcolor("black")

for i in range(6000):
    goto(heart_a(i) * 20, heart_b(i) * 20)
    for j in range(5):
        color("#f73487")
