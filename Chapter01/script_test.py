import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

#plt.switch_backend('Qt5Agg')

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(elev=25, azim=65)

xvalues = np.linspace(-4, 4, 40)
yvalues = np.linspace(-4, 4, 40)
xgrid, ygrid = np.meshgrid(xvalues, yvalues)
zvalues = xgrid**3 * ygrid + xgrid * ygrid**3
ax.plot_surface(xgrid, ygrid, zvalues, cmap=cm.coolwarm, 
    linewidth=0, antialiased=True)

print('Displaying graph')

plt.show()
