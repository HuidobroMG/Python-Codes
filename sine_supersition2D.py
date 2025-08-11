import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
X, Y = np.meshgrid(x, y)

# Centers of sources
N_SOURCES = 5
x0 = np.random.uniform(-5, 5, N_SOURCES)
y0 = np.random.uniform(-5, 5, N_SOURCES)

# Number of modes
m = 50

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
