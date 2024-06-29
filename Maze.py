"""
@author: HuidobroMG

We implement a simple algorithm to create a maze based on a random walk.
It may not have a solution, i.e. well defined starting and ending points, 
but the final output definitely has the shape of a maze.
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt
import random as rn

# Parameters of the maze
N = 50 # Sidelength of the maze
x = np.linspace(-1, 1, N)

maze = -np.ones((N, N))
visited = []

# Start in a random cell and start the path
Nx, Ny = rn.randint(0, N-1), rn.randint(0, N-1)
cell = [Nx, Ny]
maze[Nx, Ny] = 0
visited.append([Nx, Ny])

def get_neighbours(Nx, Ny):
    if 2 <= Nx < N-2 and 2 <= Ny < N-2:
        neighbours = [[Nx+2,Ny], [Nx,Ny+2], [Nx-2,Ny], [Nx,Ny-2]]
    else:
        if Nx < 2 and Ny < 2:
            neighbours = [[Nx,Ny+2], [Nx+2,Ny]]
        elif Nx < 2 and 2 <= Ny < N-2:
            neighbours = [[Nx,Ny+2], [Nx+2,Ny], [Nx,Ny-2]]
        elif Nx < 2 and Ny >= N-2:
            neighbours = [[Nx,Ny-2], [Nx+2,Ny]]
        elif Nx >= N-2 and Ny < 2:
            neighbours = [[Nx,Ny+2], [Nx-2,Ny]]
        elif Nx >= N-2 and 2 <= Ny < N-2:
            neighbours = [[Nx,Ny+2], [Nx-2,Ny], [Nx,Ny-2]]
        elif Nx >= N-2 and Ny >= N-2:
            neighbours = [[Nx,Ny-2], [Nx-2,Ny]]
        elif Ny < 2 and 2 <= Nx < N-2:
            neighbours = [[Nx,Ny+2], [Nx+2,Ny], [Nx-2,Ny]]
        elif Ny < 2 and Nx >= N-2:
            neighbours = [[Nx,Ny+2], [Nx-2,Ny]]
        elif Ny >= N-2 and Nx < 2:
            neighbours = [[Nx,Ny-2], [Nx+2,Ny]]
        elif Ny >= N-2 and 2 <= Nx < N-2:
            neighbours = [[Nx,Ny-2], [Nx+2,Ny], [Nx-2,Ny]]
            
    l = len(visited)
    for i in range(l):
        if visited[i] in neighbours:
            neighbours.remove(visited[i])
    return neighbours


# Create the maze
neighbours = get_neighbours(Nx, Ny)
comodin_neighbours = []
condition = False
idx = 0
while condition == False:
    new_cell = rn.choice(neighbours)
    visited.append(new_cell)
    
    maze[min(cell[0], new_cell[0]):max(cell[0],new_cell[0])+1,
         min(cell[1], new_cell[1]):max(cell[1],new_cell[1])+1] = 0

    neighbours = get_neighbours(new_cell[0], new_cell[1])
    if neighbours != []:
        comodin_neighbours.append(neighbours)
    else:
        # Toss a tricked coin and erase a neighbouring wall
        condition2 = False
        coin = rn.choice(['Face', 'Face', 'Down'])
        next_cell = ['up', 'down', 'left', 'right']
        if coin == 'Face':
            while condition2 == False:
                selection = rn.choice(next_cell)
                if selection == 'up' and new_cell[1] < N-1:
                    maze[new_cell[0], new_cell[1]+1] = 0
                    condition2 = True
                elif selection == 'down' and new_cell[1] > 0:
                    maze[new_cell[0], new_cell[1]-1] = 0
                    condition2 = True
                elif selection == 'left' and new_cell[0] > 0:
                    maze[new_cell[0]-1, new_cell[1]] = 0
                    condition2 = True
                elif selection == 'right' and new_cell[0] < N-1:
                    maze[new_cell[0]+1, new_cell[1]] = 0
                    condition2 = True
            condition2 = False
        while neighbours == [] and condition == False:
            new_cell = rn.choice(comodin_neighbours[idx])
            comodin_neighbours[idx].remove(new_cell)
            if comodin_neighbours[idx] == []:
                comodin_neighbours.pop(idx)
            neighbours = get_neighbours(new_cell[0], new_cell[1])
            visited.append(new_cell)
            maze[new_cell[0], new_cell[1]] = 0
            if comodin_neighbours == []:
                condition = True
                print('Finished')             
    cell = new_cell

# Plot the maze
plt.contourf(x, x, maze, levels = 2, vmin = -1, vmax = 0)
plt.show()