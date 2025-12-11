import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 401)
f = np.sin(x) * np.exp(-x**2*0.05)
df = np.cos(x) * np.exp(-x**2*0.05) + np.sin(x) * (-.1 * x) * np.exp(-x**2*0.5)

plt.plot(x, f, x, df)
plt.legend(['f(x)', 'df'])

plt.show()

def fx(x):
    return np.sin(x) * np.exp(-x**2*0.05)
def deriv(x):
    return np.cos(x) * np.exp(-x**2*0.05) + np.sin(x) * (-.1 * x) * np.exp(-x**2*0.5)


localmin = np.random.choice(x, 1)

learning_rate = 0.01
epochs = 1000

for i in range(epochs):
    grad = deriv(localmin)
    localmin = localmin - learning_rate * grad

plt.plot(x, fx(x), x, deriv(x), '--')
plt.plot(localmin, deriv(localmin), 'ro')
plt.plot(localmin, fx(localmin), 'ro')

plt.xlim(x[[0, -1]])
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x)', 'df', 'f(x) min'])
plt.title('Empirical local min {}'.format(localmin[0]))
plt.show()

###########
start_locs = np.linspace(-5, 5, 50)
final_res = np.zeros(len(start_locs))

for idx, localmin in enumerate(start_locs):
    for i in range(epochs):
        grad = deriv(localmin)
        localmin = localmin - learning_rate * grad
    
    final_res[idx] = localmin

plt.plot(start_locs, final_res, 's-')
plt.xlabel('st locs')
plt.ylabel('final guess')
plt.show()
################
learning_rates = np.linspace(1e-10, 1e-1, 50)
final_res = np.zeros(len(learning_rates))
for idx, learning_rate in enumerate(learning_rates):
    localmin = 0

    for i in range(epochs):
        grad = deriv(localmin)
        localmin = localmin - learning_rate * grad
    
    final_res[idx] = localmin

plt.plot(learning_rates, final_res, 's-')
plt.xlabel('learning rate')
plt.ylabel('final guess')
plt.show()
################
learning_rates = np.linspace(1e-10, 1e-1, 50)
epochs = np.round(np.linspace(10, 500, 40))
final_res = np.zeros((len(learning_rates), len(epochs)))
for Lidx, learning_rate in enumerate(learning_rates):

    for Eidx, epoch in enumerate(epochs):
        localmin = 0

        for i in range(int(epoch)):
            grad = deriv(localmin)
            localmin = localmin - learning_rate * grad
    
        final_res[Lidx][Eidx] = localmin

fig, ax = plt.subplots(figsize=(7, 5))
plt.imshow(final_res, extent=[learning_rates[0], learning_rates[1], epochs[0], epochs[1]], aspect='auto', origin='lower',
         vmin=-1.45, vmax=-1.2)

plt.xlabel('learning rates')
plt.ylabel('epochs')
plt.title('final guess')
plt.colorbar()
plt.show()

plt.plot(learning_rates, final_res)
plt.xlabel('learning rates')
plt.ylabel('final res')
plt.title('each line is a training epochs N')
plt.show()