import pandas as pd
import numpy as np

single = np.random.randint(0 , 100)
print(single, type(single))
row = np.random.randint(0, 100, [10])
print(row, type(row))
mat = np.random.randint(0, 100, [60, 50]) # df 61 will hide some rows, 60 wont
#print(mat, type(mat))

df = pd.DataFrame(mat)
print(df)

pd.options.display.min_rows = 5
pd.options.display.max_rows = 10
pd.options.display.max_columns = 2
pd.options.display.max_columns = None # no limit

mat = np.random.randint(0, 100, [11, 4])
df = pd.DataFrame(mat)
print(df)