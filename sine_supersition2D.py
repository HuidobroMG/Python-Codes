import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
Nx, Ny = 250, 250
x = np.linspace(-5, 5, Nx)
y = np.linspace(-5, 5, Ny)
X, Y = np.meshgrid(x, y)

# Centers of sources
N_SOURCES = 10
x0 = np.random.uniform(-5, 5, N_SOURCES)
y0 = np.random.uniform(-5, 5, N_SOURCES)

# Number of modes
m = 20

# Compute the sine of the distance from the origin
Z = 0
for i in range(1, m + 1):
    Z += np.sin(np.sqrt((X - x0[i % N_SOURCES])**2 + (Y - y0[i % N_SOURCES])**2))

# Plot the result
plt.imshow(Z, extent=(-5, 5, -5, 5), origin='lower', cmap='viridis')
plt.plot(x0, y0, 'rx')
plt.colorbar()
plt.title('2D Sine Supersition')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Evolution of a sine wave in time
t = np.linspace(0, 50, 100)
Nt = len(t)
Z_t = np.zeros((Nt, Ny, Nx))
for ti in range(Nt):
    for i in range(1, m + 1):
        Z_t[ti] += np.sin(np.sqrt((X - x0[i % N_SOURCES])**2 + (Y - y0[i % N_SOURCES])**2) - t[ti])

# Plot the result
fig, axs = plt.subplots(3, 3, figsize=(12, 12))
for i in range(9):
    axs[i // 3, i % 3].imshow(Z_t[i], extent=(-5, 5, -5, 5), origin='lower', cmap='viridis')
    axs[i // 3, i % 3].plot(x0, y0, 'rx')
    axs[i // 3, i % 3].set_title(f'Time = {t[i]:.2f}')
plt.show()

# Animate the plot in time
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(Z_t[0], extent=(-5, 5, -5, 5), origin='lower', cmap='viridis')
ax.plot(x0, y0, 'rx')
ax.set_title(f'Time = {t[0]:.2f}')

def update(frame):
    im.set_array(Z_t[frame])
    ax.set_title(f'Time = {t[frame]:.2f}')
    return im,

ani = animation.FuncAnimation(fig, update, frames=Nt, blit=False)
plt.show()
