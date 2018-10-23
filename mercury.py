import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

theta_non = np.loadtxt("theta_non.txt")
theta_ral = np.loadtxt("theta_rel.txt")

plt.plot(theta_non, "blue")
plt.plot(theta_ral, "red")

nonrelaivistic = mpatches.Patch(color='blue', label='nonrelativistic')
relativistic = mpatches.Patch(color='red', label='relativistic')
plt.legend(handles=[relativistic, nonrelaivistic])

plt.xlabel("Mercury Revolution")
plt.ylabel("Perihelion / arc secosnds")

plt.title("Perihelion Position")

plt.show()
