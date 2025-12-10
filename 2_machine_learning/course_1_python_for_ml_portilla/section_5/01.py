import numpy as np
import pandas as pd

#print(help(pd.Series))

myindex = ['qqqq', 'aaaa', 'wwww']
mydata = [1111,222 ,333]
myser = pd.Series(data=mydata)

print(myser, type(myser))

myser = pd.Series(data=mydata, index=myindex)

print(myser, type(myser))

print(myser[0])
print(myser['qqqq'])

hashmap = {"q": 1, "w":2}
ser2 = pd.Series(hashmap)
print(ser2)
print(ser2[0])