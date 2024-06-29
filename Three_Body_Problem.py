"""
@author: HuidobroMG

We solve and animate the three-body system of point particles under gravitational interactions.
The system is solved efficiently using a Runge-Kutta method of 4th order.
"""

# Import the modules
import numpy as np
import random as rn
import matplotlib.pyplot as plt
import scipy.integrate as scin
import matplotlib.animation as animation

# Parameters of the problem
m1 = 1
m2 = 5
m3 = 10

# System of differential equations
def system(t, varies):
    pos1, pos2, pos3, v1, v2, v3 = varies.reshape(6, 2)
    
    d12 = pos1 - pos2
    d13 = pos1 - pos3
    d23 = pos2 - pos3
    F12 = m1*m2*d12/np.linalg.norm(d12)
    F13 = m1*m3*d13/np.linalg.norm(d13)
    F23 = m2*m3*d23/np.linalg.norm(d23)

    ax1, ay1 = -(F12 + F13)/m1
    ax2, ay2 = (F12 - F23)/m2
    ax3, ay3 = (F13 + F23)/m3

    vx1, vy1 = v1
    vx2, vy2 = v2
    vx3, vy3 = v3
    return np.array([vx1, vy1, vx2, vy2, vx3, vy3, ax1, ay1, ax2, ay2, ax3, ay3])

# Time grid
dt = 1e-2
t_end = 20
t = np.arange(0, t_end, dt)
Nt = len(t)

# Initial conditions
pos1 = np.array([1, 5])
pos2 = np.array([-1, 5])
pos3 = np.array([0, 0])
v1 = np.array([0, 0])
v2 = np.array([0, 0])
v3 = np.array([0, 0])
vinic = np.concatenate((pos1, pos2, pos3, v1, v2, v3))

# Solve the system
sol = scin.solve_ivp(system, (0, t_end), vinic, 'RK45', t_eval = t)


# Create the animation figure
fig = plt.figure()

lim_x = 10
lim_y = 10
ax = plt.axes(xlim = (-lim_x, lim_x), ylim = (-lim_y, lim_y))

particle_1, = ax.plot([], [], 'b.')
particle_2, = ax.plot([], [], 'g.')
particle_3, = ax.plot([], [], 'r.')

def update(frame):
    particle_1.set_data([sol.y[0][frame]], [sol.y[1][frame]])
    particle_2.set_data([sol.y[2][frame]], [sol.y[3][frame]])
    particle_3.set_data([sol.y[4][frame]], [sol.y[5][frame]])
    return particle_1, particle_2, particle_3,

# Animate
ani = animation.FuncAnimation(fig = fig, func = update, 
                              frames = Nt, interval = 2*dt, blit = True)

#ani.save('3BodyProblem.gif', writer = animation.PillowWriter())
plt.show()

