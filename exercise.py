import numpy as np
import matplotlib.pyplot as plt

# Q1a, beta = 0, perfectly insulated

T_air, T_low, T_high = 30.0, 0.0, 50.0  # degrees
alpha = 1. # m^2/s
beta = 0. # 1/s
Lx = 1. # meter

x_arr = np.linspace(0,Lx,11)

"""
T_arr = 50. * x_arr 

fig = plt.figure( dpi = 100 ) # dots per inch
fig.set_size_inches(6,4)

plt.plot(x_arr, T_arr,'-b*',label = 'Analytic Solution, beta =0')
plt.xlabel(r'$x$',fontsize = 20)
plt.ylabel(r'$T$', fontsize = 20)

"""
#=====Q2a
beta = 9. # 1/s
beta_prime = beta / alpha

# solving Au = b

#A = np.array([[1.,1],[np.exp(3), np.exp(-3.)]])
A = np.array([[1.,1],[np.exp(beta_prime**0.5), np.exp(-beta_prime**0.5)]])

print A

#b = np.array([-30, 20. ])
b = np.array([T_low - T_air, T_high - T_air])
C,D = np.linalg.solve(A,b)
print C, D

temp = np.exp(beta_prime**0.5 * x_arr)
temp2 = np.exp(-beta_prime**0.5 * x_arr)
T_arr = C * temp + D * temp2 + T_air

plt.plot(x_arr, T_arr,'-r*',label = 'Analytic Solution, beta = 9')
