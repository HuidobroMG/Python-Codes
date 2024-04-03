# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:16:22 2024

@author: huido
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#------------------------------------------------------------------------------

# Number of birds
N = 100

# Limits of the grid
lim_x = 2
lim_y = 2

# Random initial positions and velocities
pos_x = lim_x*(2*np.random.rand(N) - 1)
pos_y = lim_y*(2*np.random.rand(N) - 1)
vel_x = (2*np.random.rand(N) - 1)
vel_y = (2*np.random.rand(N) - 1)
acc_x = np.zeros(N)
acc_y = np.zeros(N)

# Interaction distance between birds
flock_d = 0.5

# Maximal acceleration and velocity between birds
max_acc = 1.0
max_vel = 0.3

#------------------------------------------------------------------------------

# Evolve the system
Nt = int(1e5)
dt = 1e-2

x = np.zeros((Nt, N))
y = np.zeros((Nt, N))
for i in range(Nt):
    if i%1000 == 0:
        print('i = ', i)
    x[i] = 1.0*pos_x
    y[i] = 1.0*pos_y
    
    # Compute interactions between neighbours
    for j in range(N):
        acc_x[j] = 0
        acc_y[j] = 0
        
        rel_d = np.sqrt((pos_x[j] - pos_x)**2 + (pos_y[j] - pos_y)**2)
        neighbours = np.where((rel_d <= flock_d) & (rel_d > 0))[0]
        if neighbours.size > 0:
            # Allignment
            acc_x[j] += (2*np.mean(vel_x[neighbours]) - vel_x[j])
            acc_y[j] += (2*np.mean(vel_y[neighbours]) - vel_y[j])
            # Cohesion
            acc_x[j] += (np.mean(pos_x[neighbours]) - pos_x[j])
            acc_y[j] += (np.mean(pos_y[neighbours]) - pos_y[j])
            # Separation
            acc_x[j] += 0.2*(np.mean((pos_x[j] - pos_x[neighbours])/rel_d[neighbours]))
            acc_y[j] += 0.2*(np.mean((pos_y[j] - pos_y[neighbours])/rel_d[neighbours]))
            
            # Control the maximal value of the acceleration
            #if abs(acc_x[j]) > max_acc:
            #    acc_x[j] = acc_x[j]/abs(acc_x[j])*max_acc
            #if abs(acc_y[j]) > max_acc:
            #    acc_y[j] = acc_y[j]/abs(acc_y[j])*max_acc
            
            # Set the maximal velocity
            mod_v = np.sqrt(vel_x[j]**2 + vel_y[j]**2)
            theta = np.arctan2(vel_y[j], vel_x[j])
            if mod_v > max_vel:
                vel_x[j] = max_vel*np.cos(theta)
                vel_y[j] = max_vel*np.sin(theta)
    
    # Refresh positions and velocities
    vel_x += dt*acc_x
    vel_y += dt*acc_y
    pos_x += dt*vel_x
    pos_y += dt*vel_y
    
    # Control the movement at the edges
    edge_x1 = np.where(pos_x > lim_x)[0]
    edge_x2 = np.where(pos_x < -lim_x)[0]
    edge_y1 = np.where(pos_y > lim_y)[0]
    edge_y2 = np.where(pos_y < -lim_y)[0]
    if edge_x1.size > 0:
        pos_x[edge_x1] -= 2*lim_x
    if edge_x2.size > 0:
        pos_x[edge_x2] += 2*lim_x
    if edge_y1.size > 0:
        pos_y[edge_y1] -= 2*lim_y
    if edge_y2.size > 0:
        pos_y[edge_y2] += 2*lim_y

#------------------------------------------------------------------------------

# Create the figure
fig = plt.figure()
ax = plt.axes(xlim = (-lim_x, lim_x), ylim = (-lim_y, lim_y))

line, = ax.plot([], [], 'b.')

def update(frame):
    line.set_data(x[frame], y[frame])
    return line,

# Animate
ani = animation.FuncAnimation(fig = fig, func = update, 
                              frames = Nt, interval = 2*dt, blit = True)

#ani.save('Flock.gif', writer = animation.PillowWriter())