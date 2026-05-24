import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = 2 * x

plt.plot(x, y)
plt.show()

#####
plt.plot(x, y)
plt.title('nnn')
plt.xlabel('x')
plt.ylabel('y')

plt.xlim([0, 20])
plt.ylim([0, 20])

#plt.savefig("01.png")

plt.show()

###
#print(help(plt.savefig))
