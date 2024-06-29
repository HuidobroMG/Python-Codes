"""
@author: HuidobroMG

We show the distribution of natural and prime numbers in the plane.
The coordinates of each point is obtained as the number itself and transformed into polar coordinates.
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt

# Total of numbers
N = 10000
numbers = np.arange(1, N, 1)

#Change of coordinates
def cartesian_to_polar(x, y):
    rho = np.sqrt(x**2 + y**2)
    theta = np.arctan(y/x)
    return [rho, theta]

def polar_to_cartesian(rho, theta):
    x = rho*np.cos(theta)
    y = rho*np.sin(theta)
    return [x, y]
 
# Define the coordinates of the points
L = len(numbers)
coordinates = np.zeros((L, 2))
for i in range(L):
    coordinates[i] = polar_to_cartesian(numbers[i], numbers[i])

# Repeat the process using the prime numbers

# The Sieve of Eratosthenes
def sieve(n):
	root = int(n**0.5)
	# Initialize the list of numbers between 0 and n
	numbers = [True]*(n + 1) # At first, we consider them all prime numbers
	numbers[0] = False # The number 0 is erased
	numbers[1] = False # The number 1 is erased
	for i in range(2, root + 1): # Start the iterative process
		if numbers[i]: # If prime
			m = int(n/i - i)
			# Take the list of multiples, starting from i**2, until n, in steps of i
			numbers[i*i:n+1:i] = [False]*(m + 1) # All the multiples are erased

	# Return the list of true (prime) values
	return [i for i in range(n + 1) if numbers[i]]

numbers = sieve(N)

# Define the coordinates of the points
L = len(numbers)
coordinates2 = np.zeros((L, 2))
for i in range(L):
    coordinates2[i] = polar_to_cartesian(numbers[i], numbers[i])

# Plot the points
coordinates = coordinates.T
coordinates2 = coordinates2.T

fig = plt.figure(figsize = (13, 10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(coordinates[0], coordinates[1], 'b.')
ax2.plot(coordinates2[0], coordinates2[1], 'r.')

ax1.set_title('Natural numbers', fontsize = 12)
ax2.set_title('Prime numbers', fontsize = 12)

plt.show()
