import pandas as pd
import numpy as np

df = pd.read_csv('./ibm.csv')

print(df.head(3))
#x = df[['High', 'Low']].apply(lambda df: df['High'] > df['Low'], axis=1)
x = df[['High', 'Low']].apply(lambda row: row['High'] > row['Low'], axis=1) # is it row? use row? instead of df? check later
#x = df[['High', 'Low']].apply(lambda df: print(df), axis=1)
print(x)

def test_fun(h, l):
    return h > l

print(np.vectorize(test_fun)(df['High'], df['Low']))

y = df.iloc[0]
print("--------------")
print(y)
print("---")
print(y['High'])

print(df.describe().transpose())