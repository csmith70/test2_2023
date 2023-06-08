import matplotlib.pyplot as plt
import numpy as np

random_state = np.random.RandomState(19680801)
X = random_state.randn(10000)
#fig, ax = plt.subplots()
plt.hist(X, bins=25, normed=False)
#ax.set_xticks([])
#ax.set_yticks([])
plt.show()
