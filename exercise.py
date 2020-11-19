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
#=======

#---
def FD_Diff(h,x_0):
    f_a = np.sin(x_0 + h)
    f_b = np.sin(x_0)
    ans = 1./h * (f_a - f_b)
    return ans


n_arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
h_arr = 10.** np.array(-n_arr) #...
f_prime_FD = FD_Diff(h_arr,0.1)


Delta = abs(f_prime_FD - f_prime)
fig = plt.figure(dpi = 100)
fig.set_size_inches(6,4)

plt.plot(h_arr, Delta, '-or')
plt.xlabel('h')
plt.ylabel('error')
plt.xscale('log')
plt.yscale('log')


