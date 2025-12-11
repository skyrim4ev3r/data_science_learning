import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 2001)

def fx(x):
    return 3*x**2 - 3*x + 4

def deriv(x):
    return 6*x - 3
#############
localmin = np.random.choice(x, 1)
initval = localmin[:]

learning_rate = 0.01
epochs = 50

modelparams = np.zeros((epochs, 3))

for i in range(epochs):
    grad = deriv(localmin)
    #lr = learning_rate #fixed
    #lr = learning_rate * (1 - (i + 1)/ epochs) #time
    lr = learning_rate * np.abs(grad) #base on grad
    localmin = localmin - grad * lr

    modelparams[i][0] = localmin
    modelparams[i][1] = grad
    modelparams[i][2] = lr

plt.plot(modelparams)
plt.tight_layout()
plt.show()