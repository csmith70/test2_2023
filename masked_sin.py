# use masked arrays to plot a line with different colors by y-value
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
upper = 0.7
lower = -0.7
s_upper = np.ma.masked_where( s < upper, s)
s_lower = np.ma.masked_where( s > lower, s)
s_middle = np.ma.masked_where((np.logical_or(s > upper, s < lower)), s)

plt.ylim(-1.2,1.2)
plt.plot(t,s_upper, ls="-", lw=3.5, color="pink", label="Upper Range")
plt.plot(t,s_middle, ls=":", lw=3.5, color="black", label="Middle Range")
plt.plot(t,s_lower, ls="--", lw=3.5, color="blue", label="Lower Range")
plt.hlines(upper, t.min(), t.max())
plt.hlines(lower, np.min(t), np.max(t))
plt.legend(loc = 0)
plt.show()











