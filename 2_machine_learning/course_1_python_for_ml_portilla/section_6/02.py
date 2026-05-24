import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 10, 100)
y1 = 2 * x1

x2 = np.linspace(0, 10, 100)
y2 = x1 ** 4

fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,1,1]) # centerx, centerty, height => percent of fig?? 1 == 100?
axes1.plot(x1, y1)
axes1.set_xlim([0, 10])
axes1.set_xlabel('x')

axes2 = fig.add_axes([0.5,0.3,0.5,0.5])
axes2.plot(x2, y2)
axes2.set_xlim([0, 10]) # axes2.set_xlim(0, 10)
axes2.set_xlabel('x')

#fig.savefig('02.png')
plt.show()