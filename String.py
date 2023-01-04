# -*- coding: utf-8 -*-
"""
@author: HuidobroMG

Description:
    
    This code solve the 1-dimensional extended wave equation using finite
    differences. It differs from the standard wave equation by two additional
    terms. The point of this code is that the parameters of the equation
    are tuned such that the final result reproduces quite accurately
    a realistic string of a guitar. Indeed the vibration obtained from
    the solution to the equation is converted into sound and saved
    in a .wav file.
    
"""

#-----------------------------------------------------------------------------

# Packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.fft as fft

#-----------------------------------------------------------------------------

# Grid
L = 1 # m
dx = 0.01

# Parameters of the equation
freq = 392 # Hz
vs = freq*(2*L) # m/s
l = 2e-6 # m
gamma = 2.6e-5 # s/m**2

# Time step
dt = 0.5*dx/vs

t = np.arange(0, 2, dt)
x = np.arange(0, L+dx, dx)
Nt = len(t)
Nx = len(x)

#-----------------------------------------------------------------------------

# Matrix form of the equation
M = np.zeros((Nx, Nx))
for i in range(2, Nx-2):
    M[i, i-2] = -(l*dt*vs/dx**2)**2
    M[i,i-1] = (dt*vs/dx)**2*(1+4*(l/dx)**2)
    M[i,i] = 2 - (dt*vs)**2*(2/dx**2 + gamma/dt + 6*(l/dx**2)**2)
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

#-----------------------------------------------------------------------------

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
    
#-----------------------------------------------------------------------------

# Decompose in the frequencies
harmonics = np.zeros((9, Nt))
wave = np.zeros(Nt//10)
for i in range(9):
    for j in range(Nt):
        harmonics[i,j] = np.sum(u_t[j]*np.sin(2*np.pi*freq*(i+1)/vs*x))*dx
    wave += 100*harmonics[i, ::10]

'''
fig = plt.figure(figsize = (13, 6.5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(wave[:1000], 'b-')
ax2.plot(harmonics[0][:2000], 'b-')
'''
#-----------------------------------------------------------------------------

# Convert into audio
from scipy.io.wavfile import write

wave = wave.astype(np.float32)
write('guitar.wav', int(0.1/dt), wave)
