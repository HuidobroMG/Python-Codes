"""
@author: HuidobroMG

We simulate the Roulette game of the casino and plot the results.
In the first part of the code, we simulate the results when the bet is just red or black.
As a result, we see a decrease in the large number of bets limit since the 0 is not considered either red or black.
The slope of the straight line is precisely 1/37, the probability of 0 among the 37 possible numbers.

In the second part, we simulate the results when we bet on 1 or 2 dozens.
Although it seems that 2 dozens doubles the probability of success compared to 1 dozen,
the money bet is the double, then the losses are larger, so it has a larger (in absolute value) slope.
"""

# Import the modules
import numpy as np
import random as rn
import matplotlib.pyplot as plt
import scipy.optimize as scop

# Parameters
money = 50 # Euros
N = int(1e6) # Number of bets
bet = 1 # Bet money

# Red or black bet
counts = np.zeros(N)
for i in range(N):
    counts[i] = money
    money -= bet # The bet starts
    r = rn.randint(0, 36) # The ball is thrown
    if r%2 == 0 and r != 0: # If even, you win
        money += 2

plt.plot(counts, 'b-', label = 'Red/Black')

def line(x, m, n):
    return m*x + n

sols = scop.curve_fit(line, np.arange(N), counts)
m, n = sols[0]
print('Slope of the red/black line =', np.round(m, 4))

plt.plot(m*np.arange(N) + n, 'k-')

# One and two dozens bet
counts_1 = np.zeros(N)
counts_2 = np.zeros(N)
money_1 = 50
money_2 = 50
for i in range(N):
    counts_1[i] = money_1
    counts_2[i] = money_2
    money_1 -= bet
    money_2 -= 2*bet
    r = rn.randint(0, 36) # The ball is thrown
    if 1 <= r <= 12:
        money_1 += 3
    if 1 <= r <= 24:
        money_2 += 3

sols = scop.curve_fit(line, np.arange(N), counts_1)
m_1, n_1 = sols[0]
print('Slope of the 1 dozen line =', np.round(m_1, 4))

sols = scop.curve_fit(line, np.arange(N), counts_2)
m_2, n_2 = sols[0]
print('Slope of the 2 dozens line =', np.round(m_2, 4))

plt.plot(counts_1, 'g-', label = '1 Dozen')
plt.plot(counts_2, 'r-', label = '2 Dozens')

plt.plot(m_1*np.arange(N) + n_1, 'k-')
plt.plot(m_2*np.arange(N) + n_2, 'k-')

plt.legend(fontsize = 20)
plt.show()
