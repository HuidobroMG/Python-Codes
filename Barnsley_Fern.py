"""
@author: HuidobroMG

We construct the Barnsley fern fractal and plot the final result.
We use an iterated function system (IFS) with the appropriate affine transformations.
Modifications of the fern (called mutations) are possible by changing the affine functions f_i.
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt 
import random as rn

# Affine transformations of the Barnsley fern
f1 = np.array([0, 0, 0, 0.16, 0, 0])
f2 = np.array([0.85, 0.04, -0.04, 0.85, 0, 1.6])
f3 = np.array([0.2, -0.26, 0.23, 0.22, 0, 1.6])
f4 = np.array([-0.15, 0.28, 0.26, 0.24, 0, 0.44])

# Iteration function for each step
def iterate(pos, f):
    new_pos = np.dot(f[:-2].reshape(2, 2), pos) + f[-2:]
    return new_pos

# Number of iterations
N = int(1e5)

# Initialize the fern with a random initial position in the plane
fern = np.zeros((N, 2))
pos = np.array([0, 0])
fern[0] = pos
for i in range(N):
    p = rn.random()
    if p < 0.01:
        pos = iterate(pos, f1)
    elif p < 0.86:
        pos = iterate(pos, f2)
    elif p < 0.93:
        pos = iterate(pos, f3)
    else:
        pos = iterate(pos, f4)

    fern[i] = pos
        
# Plot
plt.plot(fern[:, 0], fern[:, 1], 'g,')
plt.axis('off')
plt.show()