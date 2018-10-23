import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x_mercury = np.loadtxt("Mercury_x_comp.txt")
y_mercury = np.loadtxt("Mercury_y_comp.txt")

x_venus = np.loadtxt("Venus_x_comp.txt")
y_venus = np.loadtxt("Venus_y_comp.txt")

x_earth = np.loadtxt("Earth_x_comp.txt")
y_earth = np.loadtxt("Earth_y_comp.txt")

x_mars = np.loadtxt("Mars_x_comp.txt")
y_mars = np.loadtxt("Mars_y_comp.txt")

x_jupiter = np.loadtxt("Jupiter_x_comp.txt")
y_jupiter = np.loadtxt("Jupiter_y_comp.txt")

x_saturn = np.loadtxt("Saturn_x_comp.txt")
y_saturn = np.loadtxt("Saturn_y_comp.txt")

x_uranus = np.loadtxt("Uranus_x_comp.txt")
y_uranus = np.loadtxt("Uranus_y_comp.txt")

x_neptune = np.loadtxt("Neptune_x_comp.txt")
y_neptune = np.loadtxt("Neptune_y_comp.txt")

x_pluto = np.loadtxt("Pluto_x_comp.txt")
y_pluto = np.loadtxt("Pluto_y_comp.txt")


x_sun = np.loadtxt("Sun_x_comp.txt")
y_sun = np.loadtxt("Sun_y_comp.txt")

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(x_pluto,y_pluto,"black")
ax1.plot(x_neptune, y_neptune,"m")
ax1.plot(x_uranus,y_uranus, "cyan")
ax1.plot(x_saturn,y_saturn, "blue")
ax1.plot(x_jupiter,y_jupiter, "red")
ax1.set_ylabel("y position / AU")
ax1.set_xlabel("x position / AU")
ax1.set_title("Outer System")

sun = mpatches.Patch(color='orange', label='sun')
mercury = mpatches.Patch(color='cyan', label='mercury')
venus = mpatches.Patch(color='red', label='venus')
earth = mpatches.Patch(color='blue', label='earth')
mars = mpatches.Patch(color='green', label='mars')
jupiter = mpatches.Patch(color='red', label='jupiter')
saturn = mpatches.Patch(color='blue', label='saturn')
uranus = mpatches.Patch(color='cyan', label='uranus')
neptune = mpatches.Patch(color='m', label='neptune')
pluto = mpatches.Patch(color='black', label='pluto')
ax1.legend(handles=[jupiter,saturn,uranus,neptune,pluto])

ax2.plot(x_mars,y_mars,"green")
ax2.plot(x_earth,y_earth, "blue")
ax2.plot(x_venus,y_venus, "red")
ax2.plot(x_mercury,y_mercury, "cyan")
ax2.set_ylabel("y position / AU")
ax2.set_xlabel("x position / AU")
ax2.set_title("Inner System")
ax2.legend(handles=[mercury,venus,earth,mars])


ax3.plot(x_sun,y_sun, "orange")
ax3.set_ylabel("y position / AU")
ax3.set_xlabel("x position / AU")
ax3.set_title("Sun motion")
ax3.legend(handles=[sun])





plt.show()
