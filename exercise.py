import numpy as np
import matplotlib.pyplot as plt

alpha = 1.
Lx = 1.
Nx = 100
hx = 0.01 # meter, spatial separation 
ht = 0.01 # seconds, time separation. 
x_arr = np.linspace(0,1, 101)   
#t_arr = np.linspace(0, 1, 101)
#PI = np.pi
PI = 3.14

#=====
fig = plt.figure( dpi = 70 ) # dots per inch
fig.set_size_inches(6,4)

t_arr = np.array([0,0.05,0.1,0.2,0.5])

for t in t_arr:
    T_analytical = np.sin(PI * x_arr) * np.exp(-PI**2 * t) + 50.
    plt.plot(x_arr, T_analytical, '-', label = "time = %5.2f s"%(t))
    
plt.legend( )
