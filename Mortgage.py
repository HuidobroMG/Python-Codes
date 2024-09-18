"""
@author: HuidobroMG

We predict the monthly payment amount and the final price of a house given some parameters of a mortgage.
In the first part we give the values mentioned above using some standard values of years, price and TIN.
Then, we also add the possibility of amortization during some desired periods of time.
In the last part we compute the values for different conditions in a mortgage to
determine the optimal conditions of a house given your requirements.
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import warnings
warnings.filterwarnings("ignore")

years = 30 # Number of years
n_dues = 12*years # Number of dues

# Tipo de interes nominal
TIN = 2.5/100 # Percentage

price = 200000 # Total price of the apartment
entry = 0.2 # Initial amount
mortgage = (1 - entry)*price # The bank mortgage loan

# Monthly amount of the mortgage using the compound interest formula
def comp_interest(mortgage, TIN, n_dues):
    r = TIN/12
    return mortgage*r*(1 + r)**n_dues/((1 + r)**n_dues - 1)

m = comp_interest(mortgage, TIN, n_dues)
total = entry*price + n_dues*m
print('Initial Value =', price)
print('Monthly amount of Mortgage ('+str(years)+' years) =', np.round(m, 2))
print('Amount of Interest =', np.round(total - price, 2))
print('Total Price =', np.round(total, 2))

# We analyze the fraction of interests and mortgage paid throughout time with and without amortization
def time_curves(TIN, n_dues, amortization_months, amortization_amount):
    monthly_interest = TIN/12
    interest_pay = []
    mortgage_pay = []
    mortgage_remain = 1.0*mortgage
    for i in range(n_dues):
        if i in amortization_months:
            interest_pay.append(monthly_interest*mortgage_remain)
            mortgage_pay.append(amortization_amount - interest_pay[i])
            mortgage_remain -= mortgage_pay[i]
        else:
            interest_pay.append(monthly_interest*mortgage_remain)
            mortgage_pay.append(m - interest_pay[i])
            mortgage_remain -= mortgage_pay[i]

        if mortgage_remain <= 0:
            mortgage_pay[i] += mortgage_remain
            n_dues = i + 1
            break
    
    return interest_pay, mortgage_pay, n_dues

print('----------------------------------')
print('No amortization')
interest_pay, mortgage_pay, n = time_curves(TIN, n_dues, [], 0)
total_interest = sum(interest_pay)
print('Amount of Interest =', np.round(total_interest, 2))

# Plot the interests and mortgage payment curves
fig, ax = plt.subplots(figsize = (12, 5))
ax.plot(range(n_dues), interest_pay, 'r-', label = 'Interests')
ax.plot(range(n_dues), mortgage_pay, 'b-', label = 'Mortgage')

# We can also add amortization in different periods of time
print('----------------------------------')
print('Amortization the first five years')
interest_pay, mortgage_pay, n = time_curves(TIN, n_dues, range(0, 5*12, 1), 1000)
total_interest = sum(interest_pay)
print('Amount of Interest =', np.round(total_interest, 2))

ax.plot(range(n), interest_pay, 'r--')
ax.plot(range(n), mortgage_pay, 'b--')

# Another possibility
print('----------------------------------')
print('Amortization between years 15 and 20')
interest_pay, mortgage_pay, n = time_curves(TIN, n_dues, range(15*12, 20*12, 1), 1000)
total_interest = sum(interest_pay)
print('Amount of Interest =', np.round(total_interest, 2))

ax.plot(range(n), interest_pay, 'r-.')
ax.plot(range(n), mortgage_pay, 'b-.')

ax.set_xlabel('Months', fontsize = 15)
ax.set_ylabel('Monthly Amount (€)', fontsize = 15)
ax.legend(fontsize = 12)


# Comparison between different conditions: high monthly due vs more time
years = np.arange(5, 40, 5)
n_dues = 12*years
price = np.linspace(100000, 220000, 15)
entry = 0.2
mortgage = (1 - entry)*price

m = np.zeros((len(price), len(years)))
total = np.zeros((len(price), len(years)))
interests = np.zeros((len(price), len(years)))
for i in range(len(price)):
    for j in range(len(n_dues)):
        m[i,j] = comp_interest(mortgage[i], TIN, n_dues[j])
        total[i,j] = entry*price[i] + n_dues[j]*m[i,j]
        interests[i,j] = total[i,j] - price[i]

# Maximal affordable values
max_m = 700 # Maximal monthly due
max_entry = 40000 # Maximal entry amount of money
max_price = max_entry/0.2
max_total = max_price/0.8 # Maximal amount of total price that we want to pay (same as fixing the amount of interests)
max_interests = max_total - max_price # Maximal amount of interests

# Graphical comparison
fig = plt.figure(figsize = (12, 6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Map of colours
cmap = plt.cm.get_cmap('hsv', len(price)+1)
cmap = LinearSegmentedColormap.from_list('gr', ["g", "r"], N = len(price))
colors = cmap(np.linspace(0, 1, len(price)+1))

# Labels
price_labels = np.round(price/1000)
for i in range(len(price)):
    ax1.plot(years, m[i], '.', color = colors[i], label = str(price_labels[i])[:-2]+'K (€)')
    ax2.plot(years, interests[i], '.', color = colors[i])

ax1.axhline(max_m, color = 'black')
ax2.axhline(max_interests, color = 'black')

ax1.set_xlabel('Years', fontsize = 15)
ax1.set_ylabel('Monthly amount', fontsize = 15)
ax2.set_xlabel('Years', fontsize = 15)
ax2.set_ylabel('Total Interests', fontsize = 15)

ax1.legend(title = 'Price of House', fontsize = 10)

fig.tight_layout()

plt.show()

