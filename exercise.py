import numpy as np
#==== Springs ===
k_01 = 1. #N/meter
k_12 = 2. #N/meter
k_23 = 3. #N/meter
k_34 = 1. #N/meter

l_01 = 1 #meters
l_12 = 1 #meters
l_23 = 1 #meters
l_34 = 1 #meters
#====Mass ===
m_1 = 0.01 #kg
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


#strain = delta L/L
#celing = ball_y[0]
"""
y1 = ball_y[1]
y2 =ball_y[2]

y1_0 = ball_y0[1]
y2_0 = ball_y0[2]
#y3 = ball_y[3]
#y4 =ball_y[4]
d_12 = abs(y2-y1)
d_12_0 = abs(y2_0 - y1_0)
strain = (d_12 - d_12_0)/d_12_0
"""

d_0 = abs(ball_y0[1:5] - ball_y0[0:4])
d_final = abs(ball_y[1:5] - ball_y[0:4])
strain = (d_final - d_0)/d_0
k_vec = np.array([k_01, k_12, k_23, k_34])
stress = k_vec * strain


fig = plt.figure( dpi = 100 )
fig.set_size_inches(6,4)
Spring_ID = [1,2,3,4]

#=====
ax1 = plt.subplot(211) # top
ax2 = plt.subplot(212) #bottom

#=====
ax1.plot(Spring_ID,strain,'ro')
ax1.set_ylabel(r'$\epsilon$')
ax1.set_ylim(0,1)
ax1.set_xlim(0,5)
#=====
ax2.plot(Spring_ID,stress,'b^')
ax2.set_ylabel(r'$\sigma$')
ax2.set_ylim(0,1)
ax2.set_xlim(0,5)
#====

plt.xticks(Spring_ID, (r'$spring_{01}$', r'$spring_{12}$', r'$spring_{23}$', r'$spring_{34}$'))

ax1.get_shared_x_axes().join(ax1, ax2)
ax1.set_xticklabels([])

