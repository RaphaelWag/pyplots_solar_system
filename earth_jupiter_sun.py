import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x_earth = np.loadtxt("Earth_x.txt")
y_earth = np.loadtxt("Earth_y.txt")

x_jupiter = np.loadtxt("Jupiter_x.txt")
y_jupiter = np.loadtxt("Jupiter_y.txt")

x_sun = np.loadtxt("Sun_x.txt")
y_sun = np.loadtxt("Sun_y.txt")

f, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x_earth,y_earth,"blue")
ax1.plot(x_jupiter, y_jupiter,"red")
ax1.plot(x_sun,y_sun, "orange")
ax1.set_ylabel("y position / AU")
ax1.set_xlabel("x position / AU")
ax1.set_title("Sun, Earth, Jupiter Motion")

ax2.plot(x_sun,y_sun,"orange")
ax2.set_ylabel("y position / AU")
ax2.set_xlabel("x position / AU")
ax2.set_title("Sun motion")

ax1.set_ylim(5.3, -5.3)
ax1.set_xlim(5.3, -5.5)

earth = mpatches.Patch(color='blue', label='earth')
jupiter = mpatches.Patch(color='red', label='jupiter')
sun = mpatches.Patch(color='orange', label='sun')
plt.legend(handles=[earth, jupiter, sun])


plt.show()
