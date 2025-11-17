import numpy as np
l1 = [1, 2, 3]
l2 = np.array(l1)
print(type(l1), type(l2))

l3 = np.arange(4,11,3)
print(l3, type(l3))

l4 = np.zeros(5, dtype=np.int16)
print(l4)
l5 = np.ones(shape=(5,5), dtype=np.float128)
print(l5)
l6 = np.ones((5,5), dtype=np.float32)
l7 = np.linspace(0, 10, 20)
print(l7)
l8 = np.linspace(start=0, stop=10, num=41)
print(l8)
l9 = np.eye(10)
print(l9)

l10 = np.random.randn(5) 
print(l10)

l11 = np.random.rand(4, 4) # [0, 1)
print(l11)

l12 = np.random.randint(0, 101, 10) 
print(l12)

np.random.seed(42)
print(np.random.rand(4))

l13 = np.ones(10)
l14 = l13.reshape(2, 5)
print(l14)

l15 = np.random.randint(0, 100, 20)
print(l15.max(), l15.min(), l15.argmin(), l15.dtype, l15.shape, l15.size)