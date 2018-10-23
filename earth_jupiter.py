import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x_earth_11 = np.loadtxt("x_earth_1_1.txt")
y_earth_11 = np.loadtxt("y_earth_1_1.txt")

x_jupiter_11 = np.loadtxt("x_jupiter_1_1.txt")
y_jupiter_11 = np.loadtxt("y_jupiter_1_1.txt")


x_earth_12 = np.loadtxt("x_earth_5_1.txt")
y_earth_12 = np.loadtxt("y_earth_5_1.txt")

x_jupiter_12 = np.loadtxt("x_jupiter_5_1.txt")
y_jupiter_12 = np.loadtxt("y_jupiter_5_1.txt")


x_earth_13 = np.loadtxt("x_earth_10_1.txt")
y_earth_13 = np.loadtxt("y_earth_10_1.txt")

x_jupiter_13 = np.loadtxt("x_jupiter_10_1.txt")
y_jupiter_13 = np.loadtxt("y_jupiter_10_1.txt")


x_earth_21 = np.loadtxt("x_earth_1_10.txt")
y_earth_21 = np.loadtxt("y_earth_1_10.txt")

x_jupiter_21 = np.loadtxt("x_jupiter_1_10.txt")
y_jupiter_21 = np.loadtxt("y_jupiter_1_10.txt")


x_earth_22 = np.loadtxt("x_earth_5_10.txt")
y_earth_22 = np.loadtxt("y_earth_5_10.txt")

x_jupiter_22 = np.loadtxt("x_jupiter_5_10.txt")
y_jupiter_22 = np.loadtxt("y_jupiter_5_10.txt")


x_earth_23 = np.loadtxt("x_earth_10_10.txt")
y_earth_23 = np.loadtxt("y_earth_10_10.txt")

x_jupiter_23 = np.loadtxt("x_jupiter_10_10.txt")
y_jupiter_23 = np.loadtxt("y_jupiter_10_10.txt")


x_earth_31 = np.loadtxt("x_earth_10_1000.txt")
y_earth_31 = np.loadtxt("y_earth_10_1000.txt")

x_jupiter_31 = np.loadtxt("x_jupiter_10_1000.txt")
y_jupiter_31 = np.loadtxt("y_jupiter_10_1000.txt")


x_earth_32 = np.loadtxt("x_earth_20_1000.txt")
y_earth_32 = np.loadtxt("y_earth_20_1000.txt")

x_jupiter_32 = np.loadtxt("x_jupiter_20_1000.txt")
y_jupiter_32 = np.loadtxt("y_jupiter_20_1000.txt")


x_earth_33 = np.loadtxt("x_earth_50_1000.txt")
y_earth_33 = np.loadtxt("y_earth_50_1000.txt")

x_jupiter_33 = np.loadtxt("x_jupiter_50_1000.txt")
y_jupiter_33 = np.loadtxt("y_jupiter_50_1000.txt")

################
###plot data ###
################

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(x_earth_11,y_earth_11,"blue")
ax1.plot(x_jupiter_11, y_jupiter_11,"red")
ax1.set_ylabel("y position / AU")
ax1.set_xlabel("x position / AU")
ax1.set_title("N=24/year")

ax2.plot(x_earth_12,y_earth_12,"blue")
ax2.plot(x_jupiter_12, y_jupiter_12,"red")
ax2.set_ylabel("y position / AU")
ax2.set_xlabel("x position / AU")
ax2.set_title("N=120/year")

ax3.plot(x_earth_13,y_earth_13,"blue")
ax3.plot(x_jupiter_13, y_jupiter_13,"red")
ax3.set_ylabel("y position / AU")
ax3.set_xlabel("x position / AU")
ax3.set_title("N=240/year")

ax1.set_ylim(5.3, -5.3)
ax2.set_ylim(5.3, -5.3)
ax3.set_ylim(5.3, -5.3)

ax1.set_xlim(5.3, -5.5)
ax2.set_xlim(5.3, -5.5)
ax3.set_xlim(5.3, -5.5)

earth = mpatches.Patch(color='blue', label='earth')
jupiter = mpatches.Patch(color='red', label='jupiter')
plt.legend(handles=[earth, jupiter])

f.suptitle("Real Jupiter Mass")

plt.show()


f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(x_earth_21,y_earth_21,"blue")
ax1.plot(x_jupiter_21, y_jupiter_21,"red")
ax1.set_ylabel("y position / AU")
ax1.set_xlabel("x position / AU")
ax1.set_title("N=24/year")

ax2.plot(x_earth_22,y_earth_22,"blue")
ax2.plot(x_jupiter_22, y_jupiter_22,"red")
ax2.set_ylabel("y position / AU")
ax2.set_xlabel("x position / AU")
ax2.set_title("N=120/year")

ax3.plot(x_earth_23,y_earth_23,"blue")
ax3.plot(x_jupiter_23, y_jupiter_23,"red")
ax3.set_ylabel("y position / AU")
ax3.set_xlabel("x position / AU")
ax3.set_title("N=240/year")



ax1.set_ylim(5.3, -5.3)
ax2.set_ylim(5.3, -5.3)
ax3.set_ylim(5.3, -5.3)

ax1.set_xlim(5.3, -5.5)
ax2.set_xlim(5.3, -5.5)
ax3.set_xlim(5.3, -5.5)

earth = mpatches.Patch(color='blue', label='earth')
jupiter = mpatches.Patch(color='red', label='jupiter')
plt.legend(handles=[earth, jupiter])

f.suptitle("Jupiter Mass * 10")

plt.show()

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(x_earth_31,y_earth_31,"blue")
ax1.plot(x_jupiter_31, y_jupiter_31,"red")
ax1.set_ylabel("y position / AU")
ax1.set_xlabel("x position / AU")
ax1.set_title("N=240/year")

ax2.plot(x_earth_32,y_earth_32,"blue")
ax2.plot(x_jupiter_32, y_jupiter_32,"red")
ax2.set_ylabel("y position / AU")
ax2.set_xlabel("x position / AU")
ax2.set_title("N=480/year")

ax3.plot(x_earth_33,y_earth_33,"blue")
ax3.plot(x_jupiter_33, y_jupiter_33,"red")
ax3.set_ylabel("y position / AU")
ax3.set_xlabel("x position / AU")
ax3.set_title("N=1200/year")


ax1.set_ylim(5.3, -5.3)
ax2.set_ylim(5.3, -5.3)
ax3.set_ylim(5.3, -5.3)

ax1.set_xlim(5.3, -5.5)
ax2.set_xlim(5.3, -5.5)
ax3.set_xlim(5.3, -5.5)

earth = mpatches.Patch(color='blue', label='earth')
jupiter = mpatches.Patch(color='red', label='jupiter')
plt.legend(handles=[earth, jupiter])

f.suptitle("Jupiter Mass * 1000")

plt.show()
