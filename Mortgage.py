"""
@author: HuidobroMG

We predict the monthly payment amount and the final price of a house given some parameters of a mortgage.
In the first part we give the values mentioned above using some standard values of years, price and TIN.
In the last part we compute the values for different conditions in a mortgage and define a weigthed index to
determine the optimal conditions of a house given your requirements.
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

years = 25 # Number of years
n_dues = 12*years # Number of dues

# Tipo de interes nominal
TIN = 2.64 # Percentage

price = 200000 # Total price of the apartment
entry = 0.2 # Initial amount
mortgage = (1 - entry)*price # The bank mortgage loan

# Monthly amount of the mortgage using the compound interest formula
def comp_interest(mortgage, TIN, n_dues):
    TIN /= 100
    r = TIN/12
    return mortgage*r*(1 + r)**n_dues/((1 + r)**n_dues - 1)

m = comp_interest(mortgage, TIN, n_dues)
total = entry*price + n_dues*m
print('Initial Value =', price)
print('Monthly amount of Mortgage (25 years) =', np.round(m, 2))
print('Total Price =', np.round(total, 2))


# Comparison between the different conditions
years = np.arange(5, 40, 5)
n_dues = 12*years
price = np.linspace(150000, 250000, 15)
entry = 0.2
mortgage = (1 - entry)*price

m = np.zeros((len(price), len(years)))
total = np.zeros((len(price), len(years)))
for i in range(len(price)):
    for j in range(len(n_dues)):
        m[i,j] = comp_interest(mortgage[i], TIN, n_dues[j])
        total[i,j] = entry*price[i] + n_dues[j]*m[i,j]

# Combined index between 0 (cheap) and 1 (expensive)
alpha = 0.5 # Multiple of the monthly amount
combined = alpha*(m - np.min(m))/(np.max(m) - np.min(m)) + (1 - alpha)*(total - np.min(total))/(np.max(total) - np.min(total))

# Maximal affordable values
max_m = 800
max_entry = 50000
max_price = max_entry/0.2
max_total = 1.2*max_price
max_combined = alpha*(max_m - np.min(m))/(np.max(m) - np.min(m)) + (1 - alpha)*(max_total - np.min(total))/(np.max(total) - np.min(total))

# Graphical comparison
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Map of colours
cmap = plt.cm.get_cmap('hsv', len(price)+1)
cmap = LinearSegmentedColormap.from_list('gr', ["g", "r"], N = len(price))
colors = cmap(np.linspace(0, 1, len(price)+1))

# Labels
price_labels = np.round(price/1000)

for i in range(len(price)):
    ax1.plot(years, m[i], '.', color = colors[i], label = str(price_labels[i])+'K')
    ax2.plot(years, total[i], '.', color = colors[i])
    ax3.plot(years, combined[i], '.', color = colors[i])

ax1.axhline(max_m, color = 'black')
ax2.axhline(max_total, color = 'black')
ax3.axhline(max_combined, color = 'black')

ax1.set_xlabel('Years', fontsize = 15)
ax1.set_ylabel('Monthly amount', fontsize = 15)
ax2.set_xlabel('Years', fontsize = 15)
ax2.set_ylabel('Total Price', fontsize = 15)
ax3.set_xlabel('Years', fontsize = 15)

ax1.legend(fontsize = 10)

fig.tight_layout()
plt.show()
