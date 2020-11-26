import numpy as np
import matplotlib.pyplot as plt
T_air, T_low, T_high = 30.0, 0.0, 50.0  # degrees
alpha = 1. # m^2/s
beta = 0. # 1/s
Lx = 1. # meter

x_arr = np.linspace(0,Lx,11)
#=== initialize A and b, all zeros
A = np.zeros([11,11]) 
b = np.zeros(11)



for i in range(1, 10):
    for j in range(1,10):
        if i == j:
            A[i,j] = -2.
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
