import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import sympy.plotting.plot as symplot

x = sym.symbols('x')
fx = 2 * x ** 2

df =sym.diff(fx, x)

print(fx)
print(df)

symplot(fx, (x, -4, 4), title='The func')
plt.show()

symplot(df, (x, -4, 4), title='The der')
plt.show()

relu = sym.Max(0, x)
sigmoid = 1 / (1 + sym.exp(-x))

p = symplot(relu, (x, -4, 4), title='Relu', show=False, line_color='blue')
p.extend(symplot(sigmoid, (x, -4, 4), title='sigmoid', show=False, line_color='red'))
p.legend = True
p.title = 'Functions'
p.show()

p = symplot(sym.diff(relu), (x, -4, 4), title='df(Relu)', show=False, line_color='blue')
p.extend(symplot(sym.diff(sigmoid), (x, -4, 4), title='df(sigmoid)', show=False, line_color='red'))
p.legend = True
p.title = 'Functions'
p.show()

#search for why vanishing gradient makes problem