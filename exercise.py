import numpy as np
import matplotlib.pyplot as plt

beta =  1.0 # kg/s
m = 1.0 # kg
g = 9.8 # m/s^2
v0 = 0. # m/s

#h = 0.01
#N = 1000
N = 1000
t_arr = np.linspace(0, 10, N+1)

v_arr_analytic = m* g / beta + (v0 - m*g/beta) * np.exp(-beta/m * t_arr)

fig = plt.figure( dpi = 70 ) # dots per inch
fig.set_size_inches(6,4)

plt.plot(t_arr, v_arr_analytic,'-k',label = 'Analytic Solution', lw = 5)

plt.xlabel(r'$t\;(\rm sec)$',fontsize = 20)
plt.ylabel(r'$v\;(\rm m/s)$', fontsize = 20)
#plt.tight_layout()
#===
v_arr = np.zeros(N+1)
v_arr[0] = 0.
for i in range(N):
    v_arr[i+1] = v_arr[i] + 0.01 * (g - beta*v_arr[i]/m)

plt.plot(t_arr, v_arr, '--r',label = 'Numerical Solution')   
plt.xlabel(r'$t\;(\rm sec)$',fontsize = 20)
plt.ylabel(r'$v\;(\rm m/s)$', fontsize = 20)

