"""
@author: HuidobroMG

We construct and represent the Mandelbrot set, which is the first example of fractal structure.
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt

# Number of points and iterations
N_points = int(1e3)
N_iters = int(5e2)

# Generate the grid and the limits
x = np.linspace(-2, 1, N_points)
y = np.linspace(-1.5, 1.5, N_points)
Mset = np.zeros((N_points, N_points))

# Construct the fractal
for i in range(N_points):
    for k in range(N_points):
        c = complex(x[i], y[k])
        z = 0 + 0j
        for u in range(N_iters):
            z = z*z + c
            if abs(z) >= 2:
                Mset[i, k] = N_iters - u
                break

# Plot using imshow()
x, y = np.meshgrid(x, y)

fig = plt.figure(figsize = (8, 8))
fig.subplots_adjust(left = 0.05, right = 0.95, bottom = 0.05, top = 0.95)
ax = fig.add_subplot(111)

ax.imshow(Mset, cmap = 'seismic', extent=[-2, 1, -1.5, 1.5])

plt.show()
