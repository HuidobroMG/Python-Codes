"""
@author: HuidobroMG

We construct an optimized version of the Sieve of Eratosthenes.
This algorithm extracts all the prime numbers between 2 and an integer number n.

The original algorithm is explained below:
We start with the first prime number (2) and erase all its multiples up to n.
The next number will be prime, so its multiples are erased as well.
This process is repeated until all the prime numbers, until n, have been extracted.

The optimized version considers i**2 as the smallest multiple of i.

An additional optimization is to start with the list of all odd numbers between 2 and n.
"""

# Define the sieve algorithm inside a function
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

n = 127
primes = sieve(n)

print('The list of all the prime numbers smaller than {}'.format(n))
print(primes)