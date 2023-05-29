import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

h = np.transpose(np.load('heights.npy'))
V = np.load('uandv.npz')
x = np.transpose(V['x'])
y = np.transpose(V['y'])
u = np.transpose(V['u'])
v = np.transpose(V['v'])

speed =  np.sqrt(u**2 + v**2)


cnt = plt.contour(h)
plt.clabel(cnt, fmt='%.0f', inline=True)
plt.show()

##Make Wind Barb Plot
plt.barbs(x, y, u, v, speed, pivot='middle')
plt.title('Wind Barbs')
plt.show()

## Make Quiver Plot
plt.quiver(x, y, u, v, speed, pivot='middle')
plt.title('Quiver Plot')
plt.show()

## Make Stream Plot
plt.streamplot(x,y,u,v)
plt.title('Stream Plot')
plt.show()
