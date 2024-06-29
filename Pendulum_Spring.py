"""
@author: HuidobroMG

We solve and animate the system of a spring which is allowed to move as a pendulum in the plane.
The system of equations may be easily extracted using the Lagrange formalism.
It is solved using a standard Runge-Kutta method of 4th order.
"""

# Import the modules
import numpy as np
import scipy.integrate as scin
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters of the problem
l0 = 1 # Natural length of the spring
m = 2 # Mass of the point particle
k = 200 # The constant of the spring
g = 9.81 # Gravity

t0 = 0
tf = 10
dt = 0.1
t = np.arange(t0, tf, dt)

# Differential equations
def eqs(t, varies):
    l, theta, l_dot, theta_dot = varies
    
    dl = l_dot
    dtheta = theta_dot
    ddl = l*dtheta**2 + g*np.cos(theta) - k/m*(l-l0)
    ddtheta = g*l*np.sin(theta) - 2*l*dl*dtheta
    return np.array([dl, dtheta, ddl, ddtheta])

# Initial conditions
l_0 = 1.2 # Initial elongation of the rope.
theta_0 = np.pi*150/180 # Initial angle.
dl_0 = 0
dtheta_0 = 0

vinic = np.array([l_0, theta_0, dl_0, dtheta_0])

# Solve the system
sols = scin.solve_ivp(eqs, (t0, tf), vinic, method = 'RK45', t_eval = t)
l, theta, dl, dtheta = sols.y


# Animate the solution
x = l*np.sin(theta)
y = l*np.cos(theta)

fig = plt.figure()
ax = plt.axes(xlim=(-1.4, 1.4), ylim=(-1.4, 1.4))
line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    thisx = [0, x[i]]
    thisy = [0, y[i]]
    
    line.set_data(thisx, thisy)
    ax.set_title('t = {}'.format(np.round(t[i], 2)))
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                        frames=int(t[-1]/dt), interval=1e3*dt, blit=True)

#anim.save('Pendulum_Spring.gif', writer = 'pillow')
plt.show()
