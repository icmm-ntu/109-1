import numpy as np
#==== Springs ===
k_01 = 1. #N/meter
k_12 = 20. #N/meter
k_23 = 1. #N/meter
k_34 = 1. #N/meter
l_01 = 1 #meters
l_12 = 1 #meters
l_23 = 1 #meters
l_34 = 1 #meters
#====Mass ===
m_1 = 0.01*10 #kg
m_2 = 0.01 #kg
m_3 = 0.01 #kg
m_4 = 0.01 #kg
#=== External, Gravity ===
g = 10. #9.8 # m/s^2
#====
A = np.array([[k_01+k_12, -k_12, 0,  0.],
              [-k_12, k_12+k_23, -k_23, 0],
              [0, -k_23, k_23+k_34, -k_34],
              [ 0.,  0., -k_34, k_34]])

print A

#===b_vec
b1 = m_1 * g + k_01 * l_01 - k_12 * l_12
b2 = m_2 * g + k_12 * l_12 - k_23 * l_23
b3 = m_3 * g + k_23 * l_23 - k_34 * l_34
b4 = m_4 * g + k_34 * l_34
b_vec = np.array([b1, b2, b3, b4])
print b_vec
# Find y 
Sol = np.linalg.solve(A,b_vec)
print Sol


import matplotlib.pyplot as plt
fig = plt.figure( dpi = 100 )
fig.set_size_inches(4,6)

#=====
ceiling_y = 0
y1,y2,y3,y4 = -Sol
#=====
ball_x = np.array([0,0,0,0,0])
ball_y = np.array([ceiling_y,y1,y2,y3,y4])
ball_y0 = np.array([0,-1,-2,-3,-4])
plt.plot(ball_x+0.1, ball_y,'-ro')
plt.plot(ball_x-0.1, ball_y0,'-ko')
plt.hlines(0, -0.2, 0.2, colors='k',lw = 10)




