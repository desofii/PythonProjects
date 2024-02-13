import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt("arraygraph.txt")
t = np.arange(data[0],data[1],data[2])
s = np.sin(2*np.pi*t)
plt.plot(t, s, label='sin(2πx)')
plt.xlabel('Axis x')
plt.ylabel('Axis y')
plt.title('My first graphic')
plt.grid(True)
plt.xlim(data[3], data[4])
plt.ylim(data[5], data[6])
plt.legend()
plt.savefig("MyFirstGraph.png")
plt.show()
