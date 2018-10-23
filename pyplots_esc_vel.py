import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x_11 = np.loadtxt("x_1_esc_vel_2.000000")
y_11 = np.loadtxt("y_1_esc_vel_2.000000")

x_12 = np.loadtxt("x_2_esc_vel_2.000000")
y_12 = np.loadtxt("y_2_esc_vel_2.000000")


x_13 = np.loadtxt("x_3_esc_vel_2.000000")
y_13 = np.loadtxt("y_3_esc_vel_2.000000")

####

x_21 = np.loadtxt("x_1_esc_vel_2.300000")
y_21 = np.loadtxt("y_1_esc_vel_2.300000")

x_22 = np.loadtxt("x_2_esc_vel_2.300000")
y_22 = np.loadtxt("y_2_esc_vel_2.300000")


x_23 = np.loadtxt("x_3_esc_vel_2.300000")
y_23 = np.loadtxt("y_3_esc_vel_2.300000")

####

x_31 = np.loadtxt("x_1_esc_vel_2.700000")
y_31 = np.loadtxt("y_1_esc_vel_2.700000")

x_32 = np.loadtxt("x_2_esc_vel_2.700000")
y_32 = np.loadtxt("y_2_esc_vel_2.700000")


x_33 = np.loadtxt("x_3_esc_vel_2.700000")
y_33 = np.loadtxt("y_3_esc_vel_2.700000")

####

x_41 = np.loadtxt("x_1_esc_vel_3.000000")
y_41 = np.loadtxt("y_1_esc_vel_3.000000")

x_42 = np.loadtxt("x_2_esc_vel_3.000000")
y_42 = np.loadtxt("y_2_esc_vel_3.000000")


x_43 = np.loadtxt("x_3_esc_vel_3.000000")
y_43 = np.loadtxt("y_3_esc_vel_3.000000")

####

x_51 = np.loadtxt("x_1_esc_vel_3.200000")
y_51 = np.loadtxt("y_1_esc_vel_3.200000")

x_52 = np.loadtxt("x_2_esc_vel_3.200000")
y_52 = np.loadtxt("y_2_esc_vel_3.200000")


x_53 = np.loadtxt("x_3_esc_vel_3.200000")
y_53 = np.loadtxt("y_3_esc_vel_3.200000")

####

f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5)

ax1.plot(x_11,y_11,"blue")
ax1.plot(x_12, y_12,"red", dashes=(4, 4))
ax1.plot(x_13,y_13,"green", dashes=(3, 3))
ax1.set_ylabel("y position / AU")
ax1.set_xlabel("x position / AU")
ax1.set_title("beta = 2")
ax1.set_ylim(-10,2)


ax2.plot(x_21,y_21,"blue")
ax2.plot(x_22, y_22,"red", dashes=(4, 4))
ax2.plot(x_23,y_23,"green", dashes=(3, 3))
ax2.set_xlabel("x position / AU")
ax2.set_title("beta = 2.3")
ax2.set_ylim(-10,2)


ax3.plot(x_31,y_31,"blue")
ax3.plot(x_32, y_32,"red", dashes=(4, 4))
ax3.plot(x_33,y_33,"green", dashes=(3, 3))
ax3.set_xlabel("x position / AU")
ax3.set_title("beta = 2.7")
ax3.set_ylim(-10,2)


ax4.plot(x_41,y_41,"blue")
ax4.plot(x_42, y_42,"red", dashes=(4, 4))
ax4.plot(x_43,y_43,"green", dashes=(3, 3))
ax4.set_xlabel("x position / AU")
ax4.set_title("beta = 3")
ax4.set_ylim(-10,2)


ax5.plot(x_51,y_51,"blue")
ax5.plot(x_52, y_52,"red", dashes=(4, 4))
ax5.plot(x_53,y_53,"green", dashes=(3, 3))
ax5.set_xlabel("x position / AU")
ax5.set_title("beta = 3.2")
ax5.set_ylim(-10,2)

ax1.set_xlim(-10,10)
ax2.set_xlim(-10,10)
ax3.set_xlim(-10,10)
ax4.set_xlim(-10,10)
ax5.set_xlim(-10,10)


v1 = mpatches.Patch(color='blue', label='v = 2*pi')
v2 = mpatches.Patch(color='red', label='v = 2*pi*1.2')
v3 = mpatches.Patch(color='green', label='v = 2*pi*1.45')
plt.legend(handles=[v1, v2, v3])

f.suptitle("Escape velocities")

plt.show()