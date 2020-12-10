import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
Nx = 21
x_arr = np.linspace(0,1, 21)

T1_arr = 50. * x_arr
T2_arr = 50. * x_arr**2.
T3_arr = -50. * x_arr**2. + 100. * x_arr
T4_arr = 50. * np.heaviside(x_arr - 0.5,  0.5)
#===== Plotting =====
fig = plt.figure( dpi = 70 ) # dots per inch
fig.set_size_inches(6,4)
plt.plot(x_arr, T1_arr , 'k-', label = r'$T_1=50x$')

plt.plot(x_arr, T2_arr, 'r-', label = r'$T_2 = 50x^2$')
plt.plot(x_arr, T3_arr, 'b-', label = r'$T_3 = -50x^2 + 100x$')


plt.plot(x_arr, T4_arr, 'g-', label = r'$T_4 = 50 \Theta(x-0.5)$')

plt.xlabel(r'$x\; \rm (m)$')
plt.ylabel(r'$T\; \rm ( ^\circ C)$')
plt.legend(loc="upper left")
plt.tight_layout()

