import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 10, 100)
y1 = 2 * x1

x2 = np.linspace(0, 10, 100)
y2 = x1 ** 4


fig, axes = plt.subplots(nrows=2, ncols=2, dpi=200, figsize=(5,8))
axes[0][0].plot(x1, y1)
axes[1][1].plot(x2, y2)
axes[1][1].set_title("nnn")

fig.subplots_adjust(wspace=1, hspace=2)
fig.suptitle("ggg", fontsize=20)

plt.show()