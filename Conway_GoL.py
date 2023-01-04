# -*- coding: utf-8 -*-
"""
@author: HuidobroMG

Description:
    
    In this code I implement a simple algorithm which tries to simulate a maze.
    It may not have a solution, i.e. well defined starting and ending points, 
    but the visualization of the maze is just nice and an enhancement
    of this code to create a correct maze may be performed.
    
"""

#-----------------------------------------------------------------------------

# Packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as rn

#-----------------------------------------------------------------------------

# Size of the grid
N = 40

# Initial configuration
init_grid = np.zeros((N, N))
Nr = 500
for i in range(Nr):
    xr = rn.randint(0, N-1)
    yr = rn.randint(0, N-1)
    init_grid[xr, yr] = 1

grid = 1*init_grid

#-----------------------------------------------------------------------------

# Function that counts the neighbours
def neighbours(i, j):
    n_neighbours = 0
    if i == 0:
        if j == 0:
            if init_grid[i+1, j] == 1:
                n_neighbours += 1
            if init_grid[i, j+1] == 1:
                n_neighbours += 1
            if init_grid[i+1, j+1] == 1:
                n_neighbours += 1
        elif j == N-1:
            if init_grid[i+1, j] == 1:
                n_neighbours += 1
            if init_grid[i, j-1] == 1:
                n_neighbours += 1
            if init_grid[i+1, j-1] == 1:
                n_neighbours += 1
        else:
            if init_grid[i+1, j] == 1:
                n_neighbours += 1
            if init_grid[i, j+1] == 1:
                n_neighbours += 1
            if init_grid[i, j-1] == 1:
                n_neighbours += 1
            if init_grid[i+1, j+1] == 1:
                n_neighbours += 1
            if init_grid[i+1, j-1] == 1:
                n_neighbours += 1
    elif i == N-1:
        if j == 0:
            if init_grid[i-1, j] == 1:
                n_neighbours += 1
            if init_grid[i, j+1] == 1:
                n_neighbours += 1
            if init_grid[i-1, j+1] == 1:
                n_neighbours += 1
        elif j == N-1:
            if init_grid[i-1, j] == 1:
                n_neighbours += 1
            if init_grid[i, j-1] == 1:
                n_neighbours += 1
            if init_grid[i-1, j-1] == 1:
                n_neighbours += 1
        else:
            if init_grid[i-1, j] == 1:
                n_neighbours += 1
            if init_grid[i-1, j-1] == 1:
                n_neighbours += 1
            if init_grid[i-1, j+1] == 1:
                n_neighbours += 1
            if init_grid[i, j-1] == 1:
                n_neighbours += 1
            if init_grid[i, j+1] == 1:
                n_neighbours += 1
    elif j == 0:
        if init_grid[i+1, j] == 1:
            n_neighbours += 1
        if init_grid[i-1, j] == 1:
            n_neighbours += 1
        if init_grid[i+1, j+1] == 1:
            n_neighbours += 1
        if init_grid[i-1, j+1] == 1:
            n_neighbours += 1
        if init_grid[i, j+1] == 1:
            n_neighbours += 1
    elif j == N-1:
        if init_grid[i+1, j] == 1:
            n_neighbours += 1
        if init_grid[i-1, j] == 1:
            n_neighbours += 1
        if init_grid[i+1, j-1] == 1:
            n_neighbours += 1
        if init_grid[i-1, j-1] == 1:
            n_neighbours += 1
        if init_grid[i, j-1] == 1:
            n_neighbours += 1
    else:
        if init_grid[i-1, j] == 1:
            n_neighbours += 1
        if init_grid[i+1, j] == 1:
            n_neighbours += 1
        if init_grid[i, j-1] == 1:
            n_neighbours += 1
        if init_grid[i, j+1] == 1:
            n_neighbours += 1
        if init_grid[i-1, j+1] == 1:
            n_neighbours += 1
        if init_grid[i-1, j-1] == 1:
            n_neighbours += 1
        if init_grid[i+1, j-1] == 1:
            n_neighbours += 1
        if init_grid[i+1, j+1] == 1:
            n_neighbours += 1
    return n_neighbours

#-----------------------------------------------------------------------------

# Iterate life
iterations = 70
grid_t = np.zeros(((N, N, iterations)))
grid_t[:, :, 0] = 1*init_grid
for i in range(1, iterations):
    for x in range(N):
        for y in range(N):        
            n = neighbours(x, y)
            if init_grid[x, y] == 1 and n < 2:
                grid[x, y] = 0
            elif init_grid[x, y] == 1 and n > 3:
                grid[x, y] = 0
            elif init_grid[x, y] == 0 and n == 3:
                grid[x, y] = 1
    grid_t[:,:, i] = 1*grid
    init_grid = 1*grid

def animate(i, img, ax):
    img.set_data(grid_t[:,:,i])
    ax.set_title('i = '+str(i))
    return img

#-----------------------------------------------------------------------------

# Animation
fig, ax = plt.subplots()
img = ax.imshow(grid_t[:,:,0], interpolation = 'nearest')
ani = animation.FuncAnimation(fig, animate, fargs = (img, ax, ),
                              frames = iterations, interval = 100,
                              repeat = False)