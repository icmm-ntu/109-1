import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
k = 1. # N/m
alpha = 0.05 # N/m^2
m = 1. # 

# Velocity Verlet Method
Nt = 5000
h = 0.01 # seconds
x_arr = np.zeros(Nt)
v_arr = np.zeros(Nt)
a_arr = np.zeros(Nt)
x0 = -10 # meters
v0 = 1. #m/s
t_arr = np.arange(Nt) * h
x_arr[0] = x0
v_arr[0] = v0
a_arr[0] = - k/m * x_arr[0] + alpha/m * x_arr[0]**2. #-w0**2.* x_arr[0] + F/m * np.cos(w1 * t_arr[0])

for n in range(0, Nt-1):
    #Step 1
    x_arr[n+1] = x_arr[n] + h * v_arr[n] + 0.5 * a_arr[n] * h**2.
    # Step 2
    a_arr[n+1] = -k/m * x_arr[n+1] + alpha/m * x_arr[n+1]**2.#-w0**2.*x_arr[n+1] + F/m * np.cos(w1 * t_arr[n+1])
    # Step 3
    v_arr[n+1] = v_arr[n] + 0.5 * (a_arr[n] + a_arr[n+1]) * h 

plt.plot(t_arr, x_arr, '--r', label="Velocity Verlet Solution")

plt.legend(loc = 'lower right')
plt.xlabel('time')
plt.ylabel('x')

