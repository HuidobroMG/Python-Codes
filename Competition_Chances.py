"""
@author: HuidobroMG

In Spain, in order to be high school teacher you need to pass an exam with several stages.
One of them consists of explaining a specific topic which is chosen by the student from a
set of balls which have been randomly extracted. 
In the mathematics speciality, there are 75 different topics, and 5 balls are extracted.

Here, we compute in two different ways the probability that at least 1 ball matches
one of the topics that you studied.
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt

Nb = 5 # Number of balls
Nt = 75 # Number of topics
Ns = 20 # Number of topics that we have studied
Nns = Nt - Ns # Number of topic that we have not studied

# Factorial function
def factorial(number):
    """
    Computes the factorial of a number number
    """
    f = 1
    for n in range(number, 1, -1):
        f *= n
    return f

# Combinatory of two numbers
def combinatorial(number_1, number_2):
    """
    Computes the combinatory of two numbers: C(number_1, number_2)
    where number_1 >= number_2
    0 <= number_2 <= number_1
    """
    return factorial(number_1)/(factorial(number_2)*factorial(number_1-number_2))

# Probabilities that at least 1 of the Nb balls has 1 of the Ns studied topics: p1, p2

# Computing the opposite and substracting it to 1
def proba_1(Nb, Nt, Nns):
    p = 1
    for i in range(Nb):
        p *= (Nns - i)/(Nt - i)
    return 1-p

# Computing all the possible outcomes which are favourable:
# The first case is: only 1 of the Nb balls have 1 of Ns studied topics
# The next cases are: 2, 3, 4... of the Nb balls have studied topics
# The last case is: all the balls have studied topics
# In each case we must compute all the possible combinations
def proba_2(Nb, Nt, Ns, Nns):    
    p = []
    p_i = 1
    for i in range(1, Nb+1):
        Nt_i = Nt-(i-1)
        Ns_i = Ns-(i-1)
        p_i *= Ns_i/Nt_i
        p.append(combin(Nb, i)*p_i)
    
    counter = 0
    p_i = 1
    for i in range(Nb-1, 0, -1):
        Nt_i = Nt-i
        Nns_i = Nns-counter
        p_i *= Nns_i/Nt_i
        
        p[i-1] *= p_i
        counter += 1
    return np.sum(p)

# Print the two probabilities
print('p1 = ', np.round(proba_1(Nb, Nt, Nns)*100, 3), '%')
print('p2 = ', np.round(proba_2(Nb, Nt, Ns, Nns)*100, 3), '%')

# Plot how the probabilities change with the number of balls and studied topics
Nb = np.arange(1, 5+1, 1)
Ns = np.arange(0, Nt+1, 1)
Nns = Nt - Ns

p = np.zeros(len(Ns))
for i in range(len(Nb)):
    for j in range(len(Ns)):
        p[j] = p1(Nb[i], Nt, Nns[j])
        
    plt.plot(Ns, p, '-', label = str(i+1)+' balls')

plt.axhline(0.9, color = 'black', label = '90% of probability')

plt.xlabel('# of studied topics', fontsize = 12)
plt.ylabel('Probability', fontsize = 12)

plt.legend()

plt.show()
