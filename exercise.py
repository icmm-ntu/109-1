import numpy as np
import matplotlib.pyplot as plt

#(a)

x = 0.1
f_prime = np.cos(x)
print f_prime
# (b) FD 
h = 0.01

f_a =np.sin(x + h)
f_b = np.sin(x)

f_prime_FD = (f_a - f_b)/h
print f_prime_FD

# (c)
