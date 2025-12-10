import pandas as pd

google = pd.read_csv("../google_stock_price.csv", usecols=["Price"]).squeeze("columns")
print(google.head())
print("------------------------")
google.add(10)
print(google.head(2))
print(google.add(10).head(2))
print(google.sub(10).head(2))
print((google + 10).head(2))
print((google * 10).head(2))
print(google.mul(10).head(2))
print(google.div(10).head(2))
print("------------------------")