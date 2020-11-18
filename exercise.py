import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(dpi = 100)
fig.set_size_inches(6,4)
x_arr = np.linspace(0,35,1001)

plt.plot(x_arr, np.exp(x_arr),'-k')
x1 = 0.1
x2 = x1 + 10 *np.pi
plt.plot(x1, np.exp(x1),'ro')
plt.plot(x2, np.exp(x2),'ro')


