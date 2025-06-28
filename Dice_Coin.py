"""
@author: HuidobroMG

This is a simple code to show the equiprobable long-term values of different (fair) random experiments.
In the first part we roll a die multiple times and show that:
1. There is no statistical significance in the discrepancies in the number of times each number appears.
2. The difference between the most and least repeated numbers decreases with the number of rolls.

In the second part, we simulate the experiment of flipping a coin 10 times.
This experiment is repeated multiple times to find the Gaussian distribution of the number of
heads in the experiment.
Although we can do the same with the dice, we chosed to perform the coin flip experiment,
since it has only two possible outcomes, compared to the six of the die.
Hence, the die experiment would require a much larger number of repetitions to see the Gaussian curve.
"""

# Import the modules
import random as rn
import numpy as np
import matplotlib.pyplot as plt

# The dice possibilites
dice_values = [1, 2, 3, 4, 5, 6]

# Number of runs
N = int(5e4)

results = []
counters = np.zeros(6)
diffs_x = []
diffs = []
for i in range(1, N):
    result = rn.choice(dice_values)  # Choose randomly
    results.append(result)
    if i % 100 == 0:
        for j in range(1, 7):
            counters[j - 1] = np.count_nonzero(np.array(results) - j)
        diffs.append(100 * (np.max(counters) - np.min(counters)) / np.min(counters))
        diffs_x.append(i)

# Plot the times each number has been obtained
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(results, bins=list(range(8)), rwidth=0.8, align="left")

ax.set_xlabel("Dice values", fontsize=12)
ax.set_ylabel("# of counts", fontsize=12)
ax.set_xlim(0, 7)

# How the differences between the times each number appears decrease with the number of runs
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(diffs_x, diffs, "-")

ax.set_xlabel("Runs", fontsize=12)
ax.set_ylabel("Mode - Antimode (%)", fontsize=12)

# --------------------------------------------------------------------------------------------

# A coin is thrown N times and we check the number of heads
N = 10

# The experiment is repeated N_EXP times
N_EXP = 5000

# The coin possibilites
coin = ["heads", "tails"]

results = np.zeros(N + 1)
for i in range(N_EXP):
    COUNTER = 0
    for j in range(N):
        result = rn.choice(coin)
        if result == "heads":
            COUNTER += 1
    results[COUNTER] += 1

# Gaussian curve
MU = N // 2  # Mean
SIGMA = np.sqrt(N / 4)  # Standard deviation

# Gaussian distribution normalized to its integral
x = np.linspace(0, N, 100)
Gauss = 1 / (SIGMA * np.sqrt(2 * np.pi)) * np.exp(-((x - MU) ** 2) / (2 * SIGMA**2))

# Plot the curve with the data points obtained from the experiments
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(list(range(N + 1)), results / N_EXP, "b.")
ax.plot(x, Gauss, "r-")

ax.set_xlabel("Number of heads", fontsize=12)
ax.set_ylabel("Normalized counts", fontsize=12)

plt.show()
