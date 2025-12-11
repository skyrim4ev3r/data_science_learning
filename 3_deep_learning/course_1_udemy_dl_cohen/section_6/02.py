# saddle point: min in 1 direction, max on other direction


#The vanishing gradient problem is a key issue in training deep neural networks, 
#particularly those with many layers. It's a phenomenon where the gradients used during backpropagation 
#(to update the weights) become exceedingly small, effectively preventing weights 
#from changing values and thus halting the learning process.

#exploding gradient: grad is so high that will pass local min to the other side
import numpy as np
import matplotlib.pyplot as plt
#from IPython import display
#display.set_matplotlib_formats('svg')

def fx(x):
    return np.cos(2*np.pi*x) + x**2

def deriv(x):
    return -2*np.pi*np.sin(2*np.pi*x) + 2*x

x = np.linspace(-2, 2, 2001)
plt.plot(x,fx(x), x, deriv(x))
plt.xlim(x[[0, -1]])
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['y', 'dy'])
plt.show()

localmin = np.random.choice(x, 1)
print(localmin)

learning_rate = 0.01
epochs = 100

for i in range(epochs):
    grad = deriv(localmin)
    localmin = localmin - learning_rate*grad

print(localmin)

plt.plot(x,fx(x), x, deriv(x))
plt.plot(localmin, deriv(localmin), 'ro')
plt.plot(localmin, fx(localmin), 'ro')
plt.xlim(x[[0, -1]])
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x)', 'df', 'f(x) min'])
plt.title("local min {}".format(localmin))
plt.show()

################################
localmin = np.random.choice(x, 1)
print(localmin)

learning_rate = 0.01
epochs = 100
modelparams = np.zeros((epochs, 2))

for i in range(epochs):
    grad = deriv(localmin)
    localmin = localmin - learning_rate*grad
    modelparams[i, :] = np.hstack((localmin.flatten(), grad.flatten())) #localmin, grad

fig, ax = plt.subplots(1, 2, figsize=(2, 4))

for i in range(2):
    ax[i].plot(modelparams[:, i], 'o-')
    ax[i].set_xlabel('iter')
    ax[i].set_ylabel("final estimate: {:0.5f}".format(localmin[0]))

ax[0].set_ylabel('local min')
ax[1].set_ylabel('der')

plt.show()