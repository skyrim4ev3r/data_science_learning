import pandas as pd

revenue = pd.read_csv("../revenue.csv", index_col="Date")
print(revenue)
print("---------------------")
print(revenue.min())
print("---------------------")
print(revenue.sum())
print("---------------------")
print(revenue.sum(axis="index"))
print(revenue.sum(axis="columns"))