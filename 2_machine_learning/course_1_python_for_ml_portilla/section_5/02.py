import pandas as pd
import numpy as np

hashmap1 = {"q": 1, "w": 2, "e": 4}
hashmap2 = {"q": 1, "w":2, "z": 6}

ser1 = pd.Series(data=hashmap1)
ser2 = pd.Series(data=hashmap2)

print(ser1.dtype)
print(ser1 + ser2)
print(ser1.add(ser2, fill_value=1000))

np.random.seed(101)
mydata = np.random.randint(0, 101, (4,3))
print(mydata)
myindex = ['ca', 'ny', 'az', 'tx']
mycol = ['jan', 'feb', 'march']

df = pd.DataFrame(mydata)
print(df)
df = pd.DataFrame(mydata, index=myindex, columns=mycol)
print(df)
print(df.info())
