import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
alpha = 1.
Lx = 1. # meters
#===== X Array =====
#Nx = 20
#h_x = float(Lx)/Nx

h_x = 0.05
Nx = 21
x_arr = h_x * (np.arange(21))
print(h_x)
print(x_arr)


#===== Time Array =====
h_t = 0.001
#Nt = 1000
Nt = 10
total_time = Nt * h_t
print ("h_t = ", h_t)
print ("total time = %.2f sec"%total_time)
t_arr = h_t * (np.arange(10))

#====
PI = np.pi
#f_arr = np.zeros(Nx+1)

T_Data = np.zeros([10, 21]) # 10 interations, 21 points
T_Data[0,] = 10.* np.sin(PI * x_arr ) + 50. # initial condition.



for n in range(0,9):
    for i in range(1, 20): ## every points from 0 to 20 except boundary points
        #f_n_i = alpha * (T_left + T_right - 2. * T_i)/hx**2
        f_n_i = alpha * (T_Data[n,i-1] + T_Data[n, i+1] - 2. * T_Data[n,i])/h_x**2.
        T_Data[n+1, i] = T_Data[n,i] + h_t * f_n_i
