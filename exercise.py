import numpy as np
import matplotlib.pyplot as plt

# Q1a, beta = 0, perfectly insulated

T_air, T_low, T_high = 30.0, 0.0, 50.0  # degrees
alpha = 1. # m^2/s
beta = 0. # 1/s
Lx = 1. # meter

x_arr = np.linspace(0,Lx,11)

T_arr = 50. * x_arr 

fig = plt.figure( dpi = 100 ) # dots per inch
fig.set_size_inches(6,4)

plt.plot(x_arr, T_arr,'-b*',label = 'Analytic Solution, beta =0')
plt.xlabel(r'$x$',fontsize = 20)
plt.ylabel(r'$T$', fontsize = 20)
