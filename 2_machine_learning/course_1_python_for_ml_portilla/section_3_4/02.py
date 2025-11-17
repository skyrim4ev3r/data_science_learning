import numpy as np

l1 = [1, 2, 3]
#l1[0:2] = 100  #err
l2 = np.array(l1)
l2[0:2] = 100
print(l2)
slice_arr = l2[0:2] # ptr to original arr
slice_arr[0:2] = 200
print(l2)
slice_arr = l2[0:2].copy()
slice_arr[0:2] = 300
print(l2, slice_arr)

l3 = np.random.randint(0, 101, 20)
bool_arr = l3 > 10
print(l3)
print(bool_arr)
print(l3[bool_arr]) #boolean indexing

print(l3 + 2)
print(l3 * l3)

l4 = np.array([0, 1,2, 3])
print(l4 // l4) # div by zero => 0
print(l4 / l4) # div by zero => nan
print(1 / l4)  # div by zero => inf
print(-1 / l4) # div by zero => -inf

print(np.sqrt(l4))
print(np.sin(l4))
print(np.arccosh(l4))
print(np.log(l4))
print(l4.var())
print(l4.sum())
print(l4.std())

l5 = np.arange(0,6).reshape(2, 3)
print(l5, l5.shape, l5.size)
print(l5.sum())
print(l5.sum(axis=0))

print(np.ones(10) * 10)

print((np.arange(1, 11) / 100).reshape(5, 2))
print((np.arange(1, 11) / 100).reshape(5, 2)[:][1])
print((np.arange(1, 11) / 100).reshape(5, 2)[:][1:2])