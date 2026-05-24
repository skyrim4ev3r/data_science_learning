import matplotlib.pyplot as plt
import numpy as np

fix, axes = plt.subplots(nrows=2, ncols=2)
print(type(axes), axes.shape)
plt.show()

x1 = np.linspace(0, 10, 100)
y1 = 2 * x1

x2 = np.linspace(0, 10, 100)
y2 = x1 ** 4

fix, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x1, y1)
axes[1].plot(x2, y2)

plt.show()

fix, axes = plt.subplots(nrows=2, ncols=2)
axes[0][0].plot(x1, y1)
axes[1][1].plot(x2, y2)

plt.show()

fig, axes = plt.subplots(nrows=2, ncols=2)

for ax_row in axes:
    for ax in ax_row:
        ax.plot(x1, y1)

fig.tight_layout()

plt.show()