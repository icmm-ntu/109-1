import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
# verlet method 
x0 = 1.0 # meters
x1 = 0.2 # meters
h = 0.01 # seconds
omega = 2. # Hz
# spring resotring force 
a1 = -omega **2 * x1
x2 = 2*x1 - x0 + a1 * h**2
Nt = 1000
t_arr = np.arange(Nt) * h
x_arr = np.zeros(Nt)
a_arr = np.zeros(Nt)
x_arr[0] = x0
x_arr[1] = x1

#
for n in range(1,Nt-1):
    a_arr[n] =  -omega **2 * x_arr[n]
    x_arr[n+1] = 2*x_arr[n] - x_arr[n-1] + a_arr[n] * h**2
    
    
plt.plot(t_arr, x_arr,'--r')
