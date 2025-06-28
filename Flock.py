"""
@author: HuidobroMG

We simulate and animate the flocking effect visible int he flight of some birds.
It is based on three simple rules stated by Craig Reynolds, which are:
Allignment (Drag force), Cohesion (Attractive force) and Separation (Repulsive force).
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Number of birds
N = 100

# Limits of the grid
LIM_X = 2
LIM_Y = 2

# Random initial positions and velocities
pos_x = LIM_X * (2 * np.random.rand(N) - 1)
pos_y = LIM_Y * (2 * np.random.rand(N) - 1)
vel_x = 2 * np.random.rand(N) - 1
vel_y = 2 * np.random.rand(N) - 1
acc_x = np.zeros(N)
acc_y = np.zeros(N)

# Interaction distance between birds
FLOCK_D = 0.5

# Maximal acceleration and velocity between birds
MAX_ACC = 1.0
MAX_VEL = 0.3

# Evolve the system in time
NT = int(2e3)
DT = 1e-2

x = np.zeros((NT, N))
y = np.zeros((NT, N))
for i in range(NT):
    if i % 200 == 0:
        print("i = ", i)
    x[i] = 1.0 * pos_x
    y[i] = 1.0 * pos_y

    # Compute the interactions between neighbours
    for j in range(N):
        acc_x[j] = 0
        acc_y[j] = 0

        rel_d = np.sqrt((pos_x[j] - pos_x) ** 2 + (pos_y[j] - pos_y) ** 2)
        neighbours = np.where((rel_d <= FLOCK_D) & (rel_d > 0))[0]
        if neighbours.size > 0:
            # Allignment
            acc_x[j] += 2 * np.mean(vel_x[neighbours]) - vel_x[j]
            acc_y[j] += 2 * np.mean(vel_y[neighbours]) - vel_y[j]
            # Cohesion
            acc_x[j] += np.mean(pos_x[neighbours]) - pos_x[j]
            acc_y[j] += np.mean(pos_y[neighbours]) - pos_y[j]
            # Separation
            acc_x[j] += 0.3 * (
                np.mean((pos_x[j] - pos_x[neighbours]) / rel_d[neighbours])
            )
            acc_y[j] += 0.3 * (
                np.mean((pos_y[j] - pos_y[neighbours]) / rel_d[neighbours])
            )

            # Control the maximal value of the acceleration
            # if abs(acc_x[j]) > max_acc:
            #    acc_x[j] = acc_x[j]/abs(acc_x[j])*max_acc
            # if abs(acc_y[j]) > max_acc:
            #    acc_y[j] = acc_y[j]/abs(acc_y[j])*max_acc

            # Set the maximal velocity
            mod_v = np.sqrt(vel_x[j] ** 2 + vel_y[j] ** 2)
            theta = np.arctan2(vel_y[j], vel_x[j])
            if mod_v > MAX_VEL:
                vel_x[j] = MAX_VEL * np.cos(theta)
                vel_y[j] = MAX_VEL * np.sin(theta)

    # Refresh positions and velocities
    vel_x += DT * acc_x
    vel_y += DT * acc_y
    pos_x += DT * vel_x
    pos_y += DT * vel_y

    # Control the movement at the edges
    edge_x1 = np.where(pos_x > LIM_X)[0]
    edge_x2 = np.where(pos_x < -LIM_X)[0]
    edge_y1 = np.where(pos_y > LIM_Y)[0]
    edge_y2 = np.where(pos_y < -LIM_Y)[0]
    if edge_x1.size > 0:
        pos_x[edge_x1] -= 2 * LIM_X
    if edge_x2.size > 0:
        pos_x[edge_x2] += 2 * LIM_X
    if edge_y1.size > 0:
        pos_y[edge_y1] -= 2 * LIM_Y
    if edge_y2.size > 0:
        pos_y[edge_y2] += 2 * LIM_Y

# Create the animation figure
fig = plt.figure()
ax = plt.axes(xlim=(-LIM_X, LIM_X), ylim=(-LIM_Y, LIM_Y))

(line,) = ax.plot([], [], "b.")

def update(frame):
    """Update the data for the animation at each frame."""
    line.set_data(x[frame], y[frame])
    return (line,)


# Animate
ani = animation.FuncAnimation(
    fig=fig, func=update, frames=NT, interval=2 * DT, blit=True
)

# ani.save('Flock.gif', writer = animation.PillowWriter())
plt.show()
