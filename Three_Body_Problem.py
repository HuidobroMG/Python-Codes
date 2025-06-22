"""
@author: HuidobroMG

We solve and animate the three-body system of point particles under gravitational interactions.
The system is solved efficiently using a Runge-Kutta method of 4th order.
"""

# Import the modules
import numpy as np
import scipy.integrate as scin
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# Parameters of the problem
MASS_1 = 1
MASS_2 = 5
MASS_3 = 10

def system(t_var, varies):
    """
    Computes the derivatives for the three-body problem.

    Parameters
    ----------
    t_var : float
        Current time (unused, required by solve_ivp).
    varies : ndarray
        Flattened array containing positions and velocities.

    Returns
    -------
    ndarray
        Derivatives of positions and velocities.
    """
    pos1, pos2, pos3, v1, v2, v3 = varies.reshape(6, 2)

    d12 = pos1 - pos2
    d13 = pos1 - pos3
    d23 = pos2 - pos3

    # Avoid division by zero
    norm_d12 = np.linalg.norm(d12) + 1e-12
    norm_d13 = np.linalg.norm(d13) + 1e-12
    norm_d23 = np.linalg.norm(d23) + 1e-12

    f12 = MASS_1 * MASS_2 * d12 / norm_d12
    f13 = MASS_1 * MASS_3 * d13 / norm_d13
    f23 = MASS_2 * MASS_3 * d23 / norm_d23

    a1 = -(f12 + f13) / MASS_1
    a2 = (f12 - f23) / MASS_2
    a3 = (f13 + f23) / MASS_3

    return np.concatenate((v1, v2, v3, a1, a2, a3))

# Time grid
DT = 1e-2
T_END = 20
TIME_GRID = np.arange(0, T_END, DT)
NT = len(TIME_GRID)

# Initial conditions
POS1 = np.array([1, 5])
POS2 = np.array([-1, 5])
POS3 = np.array([0, 0])
VEL1 = np.array([0, 0])
VEL2 = np.array([0, 0])
VEL3 = np.array([0, 0])
VINIC = np.concatenate((POS1, POS2, POS3, VEL1, VEL2, VEL3))

# Solve the system
SOL = scin.solve_ivp(system, (0, T_END), VINIC, method='RK45', t_eval=TIME_GRID)


# Create the animation figure
FIG = plt.figure()

LIM_X = 10
LIM_Y = 10
AX = plt.axes(xlim=(-LIM_X, LIM_X), ylim=(-LIM_Y, LIM_Y))

TRAIL_LENGTH = 100  # Number of frames to show in the trail

PARTICLE_1, = AX.plot([], [], 'b.')
PARTICLE_2, = AX.plot([], [], 'g.')
PARTICLE_3, = AX.plot([], [], 'r.')
TRAIL_1, = AX.plot([], [], 'b-', alpha=0.5)
TRAIL_2, = AX.plot([], [], 'g-', alpha=0.5)
TRAIL_3, = AX.plot([], [], 'r-', alpha=0.5)

def update(frame):
    """
    Animation update function.
    """
    # Current position
    PARTICLE_1.set_data([SOL.y[0][frame]], [SOL.y[1][frame]])
    PARTICLE_2.set_data([SOL.y[2][frame]], [SOL.y[3][frame]])
    PARTICLE_3.set_data([SOL.y[4][frame]], [SOL.y[5][frame]])
    # Trail indices
    start = max(0, frame - TRAIL_LENGTH)
    TRAIL_1.set_data(SOL.y[0][start:frame+1], SOL.y[1][start:frame+1])
    TRAIL_2.set_data(SOL.y[2][start:frame+1], SOL.y[3][start:frame+1])
    TRAIL_3.set_data(SOL.y[4][start:frame+1], SOL.y[5][start:frame+1])

    return PARTICLE_1, PARTICLE_2, PARTICLE_3, TRAIL_1, TRAIL_2, TRAIL_3


# Animate
ANI = animation.FuncAnimation(
    fig=FIG,
    func=update,
    frames=NT,
    interval=2 * DT,
    blit=True
)

# ANI.save('3BodyProblem.gif', writer=animation.PillowWriter())
plt.show()
