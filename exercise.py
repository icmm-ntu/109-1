import numpy as np
import matplotlib.pyplot as plt

omega = 1. #


N = 10000
h = 0.01

t_arr = np.linspace(0,100,N+1)
x_arr = np.zeros(N+1)
v_arr = np.zeros(N+1)

v0 = 0
#x0 = 1.


def ComputeK(x,v,h):
    fx = v
    fv = -omega **2. * x
    K_x = h * fx
    K_v = h * fv
    return [K_x, K_v]


x_arr[0] = 1. #amplitude of oscillation
v_arr[0] = 0. # initial velocity

for i in range(N):
    #x_new = x_old + K1_x = x_old + h * v_old
    [K1_x,K1_v] = ComputeK(x_arr[i], v_arr[i], h )
    x_mid = x_arr[i] + 0.5 * K1_x
    v_mid = v_arr[i] + 0.5 * K1_v
    #======
    [K2_x,K2_v] = ComputeK(x_mid, v_mid, h )
    x_arr[i+1] = x_arr[i] + K2_x
    v_arr[i+1] = v_arr[i] + K2_v
    
    
x_arr_analytical = 1. * np.cos(omega * t_arr)
fig = plt.figure( dpi = 70 ) # dots per inch
fig.set_size_inches(6,4)
plt.plot(t_arr, x_arr_analytical, 'k-', lw = 2, label = "Analytical Solution")
plt.plot(t_arr, x_arr, 'r--', label = "Euler Method")


   
    
    
    
