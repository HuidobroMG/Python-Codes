"""
@author: HuidobroMG

We solve the 1-dimensional extended wave equation using finite differences.
The problem differs from the standard wave equation by two additional terms.
For an optimized resolution, we express the spatial part of the PDE in matrix form.
The goal of this code is to reproduce a realistic sound of a guitar, and the result is impressive.
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.fft as fft

# Grid
L = 1 # Length of the string, [m]
dx = 0.01

# Parameters of the equation
freq = 392 # frequency of the note, [Hz]
vs = freq*(2*L) # speed of sound in the string, [m/s]
l = 2e-6 # [m]
gamma = 2.6e-5 # dispersive term parameter [s/m**2]

# Time grid
dt = 0.5*dx/vs
t = np.arange(0, 2, dt)
x = np.arange(0, L+dx, dx)
Nt = len(t)
Nx = len(x)

# Matrix form of the equation
M = np.zeros((Nx, Nx))
for i in range(2, Nx-2):
    M[i, i-2] = -(l*dt*vs/dx**2)**2
    M[i, i-1] = (dt*vs/dx)**2*(1+4*(l/dx)**2)
    M[i, i] = 2 - (dt*vs)**2*(2/dx**2 + gamma/dt + 6*(l/dx**2)**2)
    M[i, i+1] = (dt*vs/dx)**2*(1+4*(l/dx)**2)
    M[i, i+2] = -(l*dt*vs/dx**2)**2

# Initial configuration
x_p = int(2/3*Nx)
u_1 = np.linspace(0, 0.05, x_p)
u_2 = np.linspace(0.05, 0, Nx-(x_p+1))
u_0 = np.concatenate((u_1, u_2[1:]))
u_0 = np.insert(u_0, 0, 0)
u_0 = np.insert(u_0, -1, 0)
u_before = 1*u_0

# Iterate the equation
u_t = np.zeros((Nt, Nx))
for i in range(Nt):
    u_t[i] = 1*u_0
    
    u_new = np.dot(M, u_0) + u_before*(vs**2*gamma*dt - 1)
    
    u_before = 1*u_0
    u_0 = 1*u_new

# Animate the solution
Animer = 0
if Animer == 1:
    fig = plt.figure()
    ax = plt.axes(xlim=(-dx, L+dx), ylim=(1.1*np.min(u_t), 1.1*np.max(u_t)))
    line, = ax.plot([], [], lw = 3)

    def init():
        line.set_data([], [])
        return line,
    def animate(i):
        y = u_t[int(10*i)]
        line.set_data(x, y)
        ax.set_title('t = {}'.format(np.round(t[int(10*i)], 2)))
        return line,

    anim = FuncAnimation(fig, animate, init_func = init,
                         frames = 1000, interval = 10,
                         blit = True)

    #anim.save('guitar.gif', writer = 'pillow')

# Decompose in the frequencies
harmonics = np.zeros((9, Nt))
wave = np.zeros(Nt//10)
for i in range(9):
    for j in range(Nt):
        harmonics[i,j] = np.sum(u_t[j]*np.sin(2*np.pi*freq*(i+1)/vs*x))*dx
    wave += 100*harmonics[i, ::10]

# Plot the spectra
fig = plt.figure(figsize = (13, 6.5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(wave[:1000], 'b-')
ax2.plot(harmonics[0][:2000], 'b-')

plt.show()

# Convert the solution into audio
from scipy.io.wavfile import write

wave = wave.astype(np.float32)
#write('guitar_LA.wav', int(0.1/dt), wave)
