import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
data = np.loadtxt("arraysurf.txt")
v = np.arange(data[0], data[1], data[2])
u = np.arange(data[3], data[4], data[5])
theta, phi = np.meshgrid(u, v)
r = 2
X = theta * np.cos(phi)
Y = theta * np.sin(phi)
Z = r * phi
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_zlim3d(data[6], data[7])
ax.set_ylim3d(data[8], data[9])
ax.set_zlim3d(data[10], data[11])
ax.set_xlabel('Axis x')
ax.set_ylabel('Axis y')
ax.set_zlabel('Axis z')
ax.set_title('Helicoid')
surf = ax.plot_surface(X, Y, Z, cmap=cm.ocean)
fig.colorbar(surf, shrink=data[12], aspect=data[13])
plt.savefig("MyFirstSurf.png")
plt.show()
