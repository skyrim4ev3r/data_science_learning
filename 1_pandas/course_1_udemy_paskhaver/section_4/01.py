import pandas as pd

nba = pd.read_csv("../nba.csv")

print(nba)
print(nba.head())
print(nba.head(2))
print(nba.index)
print(nba.values)
print("----------------")
print(nba.shape, nba.dtypes)
print(nba.columns)
print("----------------")
print(nba.axes)
print("----------------")
print(nba.info())