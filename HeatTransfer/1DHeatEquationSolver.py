# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


"""

import numpy as np
import matplotlib.pyplot as plt

L = 0.1                        # Length in m
n = 4                          # nodes
T0 = 0                         # initial temperature; initial its scalar, will make it vector
T1s = 40                       # surface temp
T2s = 20                       # surface temp
dx = L / n                     # delta x
alpha = 8.23045e-5             #
t_final = 30                   # final 60 secs
dt = 0.1                       # time steps
x = np.linspace(dx, L, n)      # x vector
print(x)
T = np.ones(n) * T0            # vectors of n unit long
dTdt = np.empty(n)             # derivative vector
t = np.arange(0, t_final, dt)  # time vector
T[0] = 40
T[3] = 20
for j in range(1, len(t)):     # time steps
    plt.clf()
    for i in range(1, n - 1):  # spacial nodes
        dTdt[i] = alpha * (-(T[i] - T[i - 1]) / dx ** 2 + (T[i + 1] - T[i]) / dx ** 2)
        T[i] = T[i] + dTdt[i] * dt  # temp plus dTdt times delta t

    plt.figure(1)
    plt.plot(x, T, marker=".")
    plt.xticks([0.025, 0.050, 0.075, 0.1])
    plt.yticks([10, 20, 30, 40, 50])
    # plt.axis([0, L, 0, 50])
    plt.xlabel('Distance(m)')
    plt.ylabel('Temperature(C)')
    plt.draw()
    plt.pause(0.01)
plt.pause(100)
