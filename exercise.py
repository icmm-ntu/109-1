import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
# Velocity-Verlet method 
m = 1.0 # kg
F = 10. # kg * m/s^2
w0 = 1.0 # rad/s
w1 = 2.0 #rad/s
x0 = 1.0 # meters
v0 = 1.0 # m/s
h = 0.01 # seconds
Nt = 1000
t_arr = np.arange(Nt) * h

term1 = x0 * np.cos(w0 * t_arr) 
term2 = v0/w0*np.sin(w0 * t_arr)
term3 = F/(m*(w0)**2.-w1**2.)*(np.cos(w1*t_arr)-np.cos(w0*t_arr))
 
x_analytic = term1+ term2+term3
plt.plot(t_arr, x_analytic, '-k', label="Analytic Solution")


# Velocity Verlet Method
#Nt = 1000
x_arr = np.zeros(Nt)
v_arr = np.zeros(Nt)
a_arr = np.zeros(Nt)

x_arr[0] = x0
v_arr[0] = v0
a_arr[0] = -w0**2.* x_arr[0] + F/m * np.cos(w1 * t_arr[0])

for n in range(0, Nt-1):
    #Step 1
    x_arr[n+1] = x_arr[n] + h * v_arr[n] + 0.5 * a_arr[n] * h**2.
    # Step 2
    a_arr[n+1] = -w0**2.*x_arr[n+1] + F/m * np.cos(w1 * t_arr[n+1])
    # Step 3
    v_arr[n+1] = v_arr[n] + 0.5 * (a_arr[n] + a_arr[n+1]) * h 
    
    
plt.plot(t_arr, x_arr, '--r', label="Velocity Verlet Solution")

plt.legend()

