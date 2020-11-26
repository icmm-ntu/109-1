import numpy as np
import matplotlib.pyplot as plt
T_air, T_low, T_high = 30.0, 0.0, 50.0  # degrees
alpha = 1. # m^2/s
beta = 9. # 1/s
Lx = 1. # meter
beta_prime = beta / alpha
x_arr = np.linspace(0,Lx,11)
#=== initialize A and b, all zeros
A = np.zeros([11,11]) 
b = np.zeros(11)

h = 0.1 # L/10

for i in range(1, 10):
    for j in range(1,10):
        if i == j:
            A[i,j] = -2 - h**2. * beta_prime #-2.
        elif j == i+1: # non-zero off-diagonals, upper part
            A[i,j] = 1.
        elif j == i-1: # non-zero off-diagonals, lower part
            A[i,j] = 1.


#===== Boundary Conditions =====            
# Boundary Conditions for A
A[0,0]  = 1
A[1,0] = 1
A[9,10] = 1
A[10,10] =1
print A

#=====
for i in range(1, 10):
    b[i] = - h**2. * beta_prime * T_air
# Boundary Conditions for b
b[0] = T_low
b[10] = T_high
print b
# solving AT = b
#=====
T_arr = np.linalg.solve(A,b)
plt.plot(T_arr, x_arr,'b*-',label = "Numerical Solution")
#=====
