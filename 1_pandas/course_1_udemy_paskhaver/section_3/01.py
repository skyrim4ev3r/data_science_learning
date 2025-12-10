import pandas as pd

arr = ["aa", "cc", "Dd"]
x = pd.Series(arr)
print(x)

arr = [1, 3, 2]
x = pd.Series(arr)
print(x)

arr = [True, False]
x = pd.Series(arr)
print(x)

print("-------------------")
print("using hashmap: ")
arr = { "first": True, "second": False}
x = pd.Series(arr)
print(x)

print("-------------------")
x = pd.Series([2, 4, 6])
print(x.sum(), x.product(), x.std(),  x.var())
print(x.is_unique, x.size, x.values,  x.index)
print(type(x.values), type(x.index))

print("-------------------")
x = ["gg", "qq", "yy"]
y = [1, 2, 3]
print(pd.Series(data=y, index=x))