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
x_arr = h_x * (np.arange(Nx))
print(h_x)
print(x_arr)


#===== Time Array =====
h_t = 0.001
#Nt = 1000
Nt = 100
total_time = Nt * h_t
print ("h_t = ", h_t)
print ("total time = %.2f sec"%total_time)
t_arr = h_t * (np.arange(Nt))

#====
PI = np.pi
#f_arr = np.zeros(Nx+1)

T_Data = np.zeros([Nt, Nx]) # 10 interations, 21 points
T_Data[0,] = 10.* np.sin(PI * x_arr ) + 50. # initial condition.



for n in range(0,Nt-1):
    # update T_Data for all points except BCs
    for i in range(1, Nx-1): ## every points from 0 to 20 except boundary points
        #f_n_i = alpha * (T_left + T_right - 2. * T_i)/hx**2
        f_n_i = alpha * (T_Data[n,i-1] + T_Data[n, i+1] - 2. * T_Data[n,i])/h_x**2.
        T_Data[n+1, i] = T_Data[n,i] + h_t * f_n_i
    #=== update T_Data for BCs
    T_Data[n+1,0] = 50.
    T_Data[n+1,Nx-1] = 50.


#===== Plotting =====
fig = plt.figure( dpi = 150 ) # dots per inch
fig.set_size_inches(6,4)
PI = np.pi 
#n_list = [0,1,2,3,4,5,6,7,8,9]
n_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99]
for n in n_list:
    t_n = h_t * n
    T_analytic = 10.* np.sin(PI * x_arr )* np.exp(-PI**2 * t_n) + 50.
    plt.plot(x_arr, T_analytic , '-',  label = 'time = %.2f sec'%(t_n))
    plt.plot(x_arr, T_Data[n,:] , '--')

plt.xlim(0,1)
plt.ylim(30,45)
plt.xlabel(r'$x\; \rm (m)$')
plt.ylabel(r'$T\; \rm ( ^\circ C)$')
plt.legend(loc="upper left")
plt.tight_layout()

#===== check_Von_Neumann Criterion 
gamma = alpha * h_t/h_x**2 
if gamma > 1/2.:
    print ("Von_Neumann Unstable, gamma = %.2f!!!"%gamma)
else:
    print  ("Von_Neumann Stable, gamma = %.2f"%gamma)

plt.xlim(0,1)
plt.ylim(45,65)
plt.xlabel(r'$x\; \rm (m)$')
plt.ylabel(r'$T\; \rm ( ^\circ C)$')
plt.legend(loc="upper left")
plt.tight_layout()
#plt.savefig("Figs/TimeEvolution_HeatEq_beta_0_Euler.png")
