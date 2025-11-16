import numpy as np
import sympy as sym
from IPython.display import display

x = sym.symbols('x')

fx = 2*x**2
gx = 4*x**3 - 3*x**4

df =sym.diff(fx)
dg = sym.diff(gx)

manual =df*gx + fx*dg
viasympy = sym.diff(fx*gx)

print('functions')
display(fx)
display(gx)

print('ders')
display(df)
display(dg)
print('prod')
display(manual)
print('via sympy')
display(viasympy)

fx = (x ** 2 + 4 * x ** 3) ** 5
display(fx)
display(sym.diff(fx))
