import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
alpha = 1.0
Lx = 1. # meters
#===== X Array =====
h_x = 0.05
Nx = 21
x_arr = h_x * (np.arange(Nx))
#===== Time Array =====
h_t = 0.001
Nt = 100
total_time = Nt * h_t
print ("h_t = ", h_t)
print ("total time = %.2f sec"%total_time)
t_arr = h_t * (np.arange(Nt))
#====
T_Data = np.zeros([Nt, Nx]) # 10 interations, 21 points
# Initial Condition
T1_arr = 50. * x_arr
T2_arr = 50. * x_arr**2
T3_arr = -50. * x_arr**2 + 100. * x_arr
T4_arr = 50 * np.heaviside(x_arr - 0.5, 0.5) 
T_Data[0,] = T4_arr
                
    
for n in range(0,Nt-1):
    # update T_Data for all points except BCs
    for i in range(1, Nx-1): ## every points from 0 to 20 except boundary points
        f_n_i = alpha * (T_Data[n,i-1] + T_Data[n, i+1] - 2. * T_Data[n,i])/h_x**2.
        T_Data[n+1, i] = T_Data[n,i] + h_t * f_n_i
    #=== update T_Data for BCs
    T_Data[n+1,0] = 0.
    T_Data[n+1,Nx-1] = 50.



#===== Plotting =====
fig = plt.figure( dpi = 150 ) # dots per inch
fig.set_size_inches(6,4)
#PI = np.pi 
#n_list = [0,1,2,3,4,5,6,7,8,9]
n_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99]
for n in n_list:
    t_n = h_t * n
    plt.plot(x_arr, T_Data[n,:] , '--', label = 'time = %.2f sec'%(t_n))

plt.xlim(0,1)
plt.ylim(0,55)
plt.xlabel(r'$x\; \rm (m)$')
plt.ylabel(r'$T\; \rm ( ^\circ C)$')
plt.legend(loc="upper left")
plt.tight_layout()


