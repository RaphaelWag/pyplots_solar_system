#Author: Raphael Wagner 6.10.2018

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

###########################
###read in data from cpp###
###########################
ang_mom_euler_object_circular_1 = np.loadtxt("ang_momentum_euler_object_circular_120.txt")
ang_mom_verlet_object_circular_1 = np.loadtxt("ang_momentum_verlet_object_circular_120.txt")
E_kin_euler_object_circular_1 = np.loadtxt("E_kin_euler_object_circular_120.txt")
E_pot_euler_object_circular_1 = np.loadtxt("E_pot_euler_object_circular_120.txt")
E_kin_verlet_object_circular_1 = np.loadtxt("E_kin_verlet_object_circular_120.txt")
E_pot_verlet_object_circular_1 = np.loadtxt("E_pot_verlet_object_circular_120.txt")


pos_x_euler_object_circular_1 = np.loadtxt("pos_x_euler_object_circular_120.txt")
pos_y_euler_object_circular_1 = np.loadtxt("pos_y_euler_object_circular_120.txt")
pos_z_euler_object_circular_1 = np.loadtxt("pos_z_euler_object_circular_120.txt")
pos_x_verlet_object_circular_1 = np.loadtxt("pos_x_verlet_object_circular_120.txt")
pos_y_verlet_object_circular_1 = np.loadtxt("pos_y_verlet_object_circular_120.txt")
pos_z_verlet_object_circular_1 = np.loadtxt("pos_z_verlet_object_circular_120.txt")

ang_mom_euler_circular_1 = np.loadtxt("ang_momentum_euler_circular_120.txt")
ang_mom_verlet_circular_1 = np.loadtxt("ang_momentum_verlet_circular_120.txt")
E_kin_euler_circular_1 = np.loadtxt("E_kin_euler_circular_120.txt")
E_pot_euler_circular_1 = np.loadtxt("E_pot_euler_circular_120.txt")
E_kin_verlet_circular_1 = np.loadtxt("E_kin_verlet_circular_120.txt")
E_pot_verlet_circular_1 = np.loadtxt("E_pot_verlet_circular_120.txt")

pos_x_euler_circular_1 = np.loadtxt("pos_x_euler_circular_120.txt")
pos_y_euler_circular_1 = np.loadtxt("pos_y_euler_circular_120.txt")
pos_z_euler_circular_1 = np.loadtxt("pos_z_euler_circular_120.txt")
pos_x_verlet_circular_1 = np.loadtxt("pos_x_verlet_circular_120.txt")
pos_y_verlet_circular_1 = np.loadtxt("pos_y_verlet_circular_120.txt")
pos_z_verlet_circular_1 = np.loadtxt("pos_z_verlet_circular_120.txt")

ang_mom_euler_object_circular_2 = np.loadtxt("ang_momentum_euler_object_circular_240.txt")
ang_mom_verlet_object_circular_2 = np.loadtxt("ang_momentum_verlet_object_circular_240.txt")
E_kin_euler_object_circular_2 = np.loadtxt("E_kin_euler_object_circular_240.txt")
E_pot_euler_object_circular_2 = np.loadtxt("E_pot_euler_object_circular_240.txt")
E_kin_verlet_object_circular_2 = np.loadtxt("E_kin_verlet_object_circular_240.txt")
E_pot_verlet_object_circular_2 = np.loadtxt("E_pot_verlet_object_circular_240.txt")

pos_x_euler_object_circular_2 = np.loadtxt("pos_x_euler_object_circular_240.txt")
pos_y_euler_object_circular_2 = np.loadtxt("pos_y_euler_object_circular_240.txt")
pos_z_euler_object_circular_2 = np.loadtxt("pos_z_euler_object_circular_240.txt")
pos_x_verlet_object_circular_2 = np.loadtxt("pos_x_verlet_object_circular_240.txt")
pos_y_verlet_object_circular_2 = np.loadtxt("pos_y_verlet_object_circular_240.txt")
pos_z_verlet_object_circular_2 = np.loadtxt("pos_z_verlet_object_circular_240.txt")

ang_mom_euler_circular_2 = np.loadtxt("ang_momentum_euler_circular_240.txt")
ang_mom_verlet_circular_2 = np.loadtxt("ang_momentum_verlet_circular_240.txt")
E_kin_euler_circular_2 = np.loadtxt("E_kin_euler_circular_240.txt")
E_pot_euler_circular_2 = np.loadtxt("E_pot_euler_circular_240.txt")
E_kin_verlet_circular_2 = np.loadtxt("E_kin_verlet_circular_240.txt")
E_pot_verlet_circular_2 = np.loadtxt("E_pot_verlet_circular_240.txt")

pos_x_euler_circular_2 = np.loadtxt("pos_x_euler_circular_240.txt")
pos_y_euler_circular_2 = np.loadtxt("pos_y_euler_circular_240.txt")
pos_z_euler_circular_2 = np.loadtxt("pos_z_euler_circular_240.txt")
pos_x_verlet_circular_2 = np.loadtxt("pos_x_verlet_circular_240.txt")
pos_y_verlet_circular_2 = np.loadtxt("pos_y_verlet_circular_240.txt")
pos_z_verlet_circular_2 = np.loadtxt("pos_z_verlet_circular_240.txt")

ang_mom_euler_object_circular_3 = np.loadtxt("ang_momentum_euler_object_circular_480.txt")
ang_mom_verlet_object_circular_3 = np.loadtxt("ang_momentum_verlet_object_circular_480.txt")
E_kin_euler_object_circular_3 = np.loadtxt("E_kin_euler_object_circular_480.txt")
E_pot_euler_object_circular_3 = np.loadtxt("E_pot_euler_object_circular_480.txt")
E_kin_verlet_object_circular_3 = np.loadtxt("E_kin_verlet_object_circular_480.txt")
E_pot_verlet_object_circular_3 = np.loadtxt("E_pot_verlet_object_circular_480.txt")

pos_x_euler_object_circular_3 = np.loadtxt("pos_x_euler_object_circular_480.txt")
pos_y_euler_object_circular_3 = np.loadtxt("pos_y_euler_object_circular_480.txt")
pos_z_euler_object_circular_3 = np.loadtxt("pos_z_euler_object_circular_480.txt")
pos_x_verlet_object_circular_3 = np.loadtxt("pos_x_verlet_object_circular_480.txt")
pos_y_verlet_object_circular_3 = np.loadtxt("pos_y_verlet_object_circular_480.txt")
pos_z_verlet_object_circular_3 = np.loadtxt("pos_z_verlet_object_circular_480.txt")

ang_mom_euler_circular_3 = np.loadtxt("ang_momentum_euler_circular_480.txt")
ang_mom_verlet_circular_3 = np.loadtxt("ang_momentum_verlet_circular_480.txt")
E_kin_euler_circular_3 = np.loadtxt("E_kin_euler_circular_480.txt")
E_pot_euler_circular_3 = np.loadtxt("E_pot_euler_circular_480.txt")
E_kin_verlet_circular_3 = np.loadtxt("E_kin_verlet_circular_480.txt")
E_pot_verlet_circular_3 = np.loadtxt("E_pot_verlet_circular_480.txt")

pos_x_euler_circular_3 = np.loadtxt("pos_x_euler_circular_480.txt")
pos_y_euler_circular_3 = np.loadtxt("pos_y_euler_circular_480.txt")
pos_z_euler_circular_3 = np.loadtxt("pos_z_euler_circular_480.txt")
pos_x_verlet_circular_3 = np.loadtxt("pos_x_verlet_circular_480.txt")
pos_y_verlet_circular_3 = np.loadtxt("pos_y_verlet_circular_480.txt")
pos_z_verlet_circular_3 = np.loadtxt("pos_z_verlet_circular_480.txt")

################
###plot data ###
################

###########################################
###conserved quantaties for N = 120/year###
###########################################


timesteps = np.arange(0,240,1,dtype=int)

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(timesteps,E_kin_euler_object_circular_1,"blue")
ax1.plot(timesteps, E_kin_euler_circular_1,"red", dashes=(4, 4))
ax1.plot(timesteps,E_kin_verlet_object_circular_1,"green", dashes=(3, 3))
ax1.plot(timesteps, E_kin_verlet_circular_1, "cyan", dashes=(4, 4))
ax1.set_ylabel("Kinetic Energy")
ax1.set_xlabel("Timesteps*N")
ax1.set_ylim(0.1, -0.1)


ax2.plot(timesteps,E_pot_euler_object_circular_1,"blue")
ax2.plot(timesteps, E_pot_euler_circular_1,"red",dashes=(4, 4))
ax2.plot(timesteps,E_pot_verlet_object_circular_1,"green", dashes=(3, 3))
ax2.plot(timesteps, E_pot_verlet_circular_1, "cyan", dashes=(4, 4))
ax2.set_ylabel("Potential Energy")
ax2.set_xlabel("Timesteps*N")
ax2.set_ylim(0.1, -0.1)

ax3.plot(timesteps,ang_mom_euler_object_circular_1,"blue")
ax3.plot(timesteps, ang_mom_euler_circular_1,"red")
ax3.plot(timesteps,ang_mom_verlet_object_circular_1,"green", dashes=(3, 3))
ax3.plot(timesteps, ang_mom_verlet_circular_1, "cyan", dashes=(4, 4))
ax3.set_ylabel("Angular Momentum")
ax3.set_xlabel("Timesteps*N")
ax3.set_ylim(0.1, -0.1)

euler = mpatches.Patch(color='red', label='euler')
euler_object = mpatches.Patch(color='blue', label='euler object')
verlet_object = mpatches.Patch(color='green', label='verlet object')
verlet = mpatches.Patch(color='cyan', label='verlet')
plt.legend(handles=[euler, verlet, euler_object, verlet_object])

f.suptitle("N=120 / year")

plt.show()

###################################
###positions for N = 120 / year ###
###################################

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(pos_x_euler_object_circular_1,pos_y_euler_object_circular_1,"blue")
ax1.plot(pos_x_euler_circular_1,pos_y_euler_circular_1, "red", dashes=(4, 4))
ax1.set_ylabel("y position / AU")
ax1.set_xlabel("x position / AU")
ax1.set_title("Euler method")

ax2.plot(pos_y_verlet_object_circular_1, pos_x_verlet_object_circular_1, "green",dashes=(7,7))
ax2.plot(pos_x_verlet_circular_1, pos_y_verlet_circular_1, "cyan", dashes=(10, 10))
ax2.set_ylabel("y position / AU")
ax2.set_xlabel("x position / AU")
ax2.set_title("Verlet Method ")

ax3.plot(timesteps,pos_z_euler_object_circular_1,"blue")
ax3.plot(timesteps,pos_z_euler_circular_1,"green", dashes=(4, 4))
ax3.plot(timesteps,pos_z_verlet_object_circular_1,"red", dashes=(3, 3))
ax3.plot(timesteps,pos_z_verlet_circular_1, "cyan", dashes=(5, 5))
ax3.set_ylabel("z position / AU")
ax3.set_xlabel("timesteps*N")
ax3.set_title("z axis movement")

euler = mpatches.Patch(color='green', label='euler')
euler_object = mpatches.Patch(color='blue', label='euler object')
verlet_object = mpatches.Patch(color='red', label='verlet object')
verlet = mpatches.Patch(color='cyan', label='verlet')
plt.legend(handles=[euler, verlet, euler_object, verlet_object])

f.suptitle("N=120 / year")

plt.show()


###########################################
###conserved quantaties for N = 240/year###
###########################################


timesteps = np.arange(0,240,1,dtype=int)

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(timesteps,E_kin_euler_object_circular_2,"blue")
ax1.plot(timesteps, E_kin_euler_circular_2,"red", dashes=(4, 4))
ax1.plot(timesteps,E_kin_verlet_object_circular_2,"green", dashes=(3, 3))
ax1.plot(timesteps, E_kin_verlet_circular_2, "cyan", dashes=(4, 4))
ax1.set_ylabel("Kinetic Energy")
ax1.set_xlabel("Timesteps*N")
ax1.set_ylim(0.1, -0.1)


ax2.plot(timesteps,E_pot_euler_object_circular_2,"blue")
ax2.plot(timesteps, E_pot_euler_circular_2,"red",dashes=(4, 4))
ax2.plot(timesteps,E_pot_verlet_object_circular_2,"green", dashes=(3, 3))
ax2.plot(timesteps, E_pot_verlet_circular_2, "cyan", dashes=(4, 4))
ax2.set_ylabel("Potential Energy")
ax2.set_xlabel("Timesteps*N")
ax2.set_ylim(0.1, -0.1)

ax3.plot(timesteps,ang_mom_euler_object_circular_2,"blue")
ax3.plot(timesteps, ang_mom_euler_circular_2,"red")
ax3.plot(timesteps,ang_mom_verlet_object_circular_2,"green", dashes=(3, 3))
ax3.plot(timesteps, ang_mom_verlet_circular_2, "cyan", dashes=(4, 4))
ax3.set_ylabel("Angular Momentum")
ax3.set_xlabel("Timesteps*N")
ax3.set_ylim(0.1, -0.1)

euler = mpatches.Patch(color='red', label='euler')
euler_object = mpatches.Patch(color='blue', label='euler object')
verlet_object = mpatches.Patch(color='green', label='verlet object')
verlet = mpatches.Patch(color='cyan', label='verlet')
plt.legend(handles=[euler, verlet, euler_object, verlet_object])

f.suptitle("N=240 / year")

plt.show()

###################################
###positions for N = 240 / year ###
###################################

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(pos_x_euler_object_circular_2,pos_y_euler_object_circular_2,"blue")
ax1.plot(pos_x_euler_circular_2,pos_y_euler_circular_2, "red", dashes=(4, 4))
ax1.set_ylabel("y position / AU")
ax1.set_xlabel("x position / AU")
ax1.set_title("Euler method")

ax2.plot(pos_y_verlet_object_circular_2, pos_x_verlet_object_circular_2, "green",dashes=(7,7))
ax2.plot(pos_x_verlet_circular_2, pos_y_verlet_circular_2, "cyan", dashes=(10, 10))
ax2.set_ylabel("y position / AU")
ax2.set_xlabel("x position / AU")
ax2.set_title("Verlet Method ")

ax3.plot(timesteps,pos_z_euler_object_circular_2,"blue")
ax3.plot(timesteps,pos_z_euler_circular_2,"green", dashes=(4, 4))
ax3.plot(timesteps,pos_z_verlet_object_circular_2,"red", dashes=(3, 3))
ax3.plot(timesteps,pos_z_verlet_circular_2, "cyan", dashes=(5, 5))
ax3.set_ylabel("z position / AU")
ax3.set_xlabel("timesteps*N")
ax3.set_title("z axis movement")

euler = mpatches.Patch(color='green', label='euler')
euler_object = mpatches.Patch(color='blue', label='euler object')
verlet_object = mpatches.Patch(color='red', label='verlet object')
verlet = mpatches.Patch(color='cyan', label='verlet')
plt.legend(handles=[euler, verlet, euler_object, verlet_object])

f.suptitle("N=240 / year")

plt.show()

###########################################
###conserved quantaties for N = 480/year###
###########################################


timesteps = np.arange(0,240,1,dtype=int)

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(timesteps,E_kin_euler_object_circular_3,"blue")
ax1.plot(timesteps, E_kin_euler_circular_3,"red", dashes=(4, 4))
ax1.plot(timesteps,E_kin_verlet_object_circular_3,"green", dashes=(3, 3))
ax1.plot(timesteps, E_kin_verlet_circular_3, "cyan", dashes=(4, 4))
ax1.set_ylabel("Kinetic Energy")
ax1.set_xlabel("Timesteps*N")
ax1.set_ylim(0.1, -0.1)


ax2.plot(timesteps,E_pot_euler_object_circular_3,"blue")
ax2.plot(timesteps, E_pot_euler_circular_3,"red",dashes=(4, 4))
ax2.plot(timesteps,E_pot_verlet_object_circular_3,"green", dashes=(3, 3))
ax2.plot(timesteps, E_pot_verlet_circular_3, "cyan", dashes=(4, 4))
ax2.set_ylabel("Potential Energy")
ax2.set_xlabel("Timesteps*N")
ax2.set_ylim(0.1, -0.1)

ax3.plot(timesteps,ang_mom_euler_object_circular_3,"blue")
ax3.plot(timesteps, ang_mom_euler_circular_3,"red")
ax3.plot(timesteps,ang_mom_verlet_object_circular_3,"green", dashes=(3, 3))
ax3.plot(timesteps, ang_mom_verlet_circular_3, "cyan", dashes=(4, 4))
ax3.set_ylabel("Angular Momentum")
ax3.set_xlabel("Timesteps*N")
ax3.set_ylim(0.1, -0.1)

euler = mpatches.Patch(color='red', label='euler')
euler_object = mpatches.Patch(color='blue', label='euler object')
verlet_object = mpatches.Patch(color='green', label='verlet object')
verlet = mpatches.Patch(color='cyan', label='verlet')
plt.legend(handles=[euler, verlet, euler_object, verlet_object])

f.suptitle("N=480 / year")

plt.show()

###################################
###positions for N = 480 / year ###
###################################

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(pos_x_euler_object_circular_3,pos_y_euler_object_circular_3,"blue")
ax1.plot(pos_x_euler_circular_3,pos_y_euler_circular_3, "red", dashes=(4, 4))
ax1.set_ylabel("y position / AU")
ax1.set_xlabel("x position / AU")
ax1.set_title("Euler method")

ax2.plot(pos_y_verlet_object_circular_3, pos_x_verlet_object_circular_3, "green",dashes=(7,7))
ax2.plot(pos_x_verlet_circular_3, pos_y_verlet_circular_3, "cyan", dashes=(10, 10))
ax2.set_ylabel("y position / AU")
ax2.set_xlabel("x position / AU")
ax2.set_title("Verlet Method ")

ax3.plot(timesteps,pos_z_euler_object_circular_3,"blue")
ax3.plot(timesteps,pos_z_euler_circular_3,"green", dashes=(4, 4))
ax3.plot(timesteps,pos_z_verlet_object_circular_3,"red", dashes=(3, 3))
ax3.plot(timesteps,pos_z_verlet_circular_3, "cyan", dashes=(5, 5))
ax3.set_ylabel("z position / AU")
ax3.set_xlabel("timesteps *N")
ax3.set_title("z axis movement")

euler = mpatches.Patch(color='green', label='euler')
euler_object = mpatches.Patch(color='blue', label='euler object')
verlet_object = mpatches.Patch(color='red', label='verlet object')
verlet = mpatches.Patch(color='cyan', label='verlet')
plt.legend(handles=[euler, verlet, euler_object, verlet_object])

f.suptitle("N=480 / year")

plt.show()