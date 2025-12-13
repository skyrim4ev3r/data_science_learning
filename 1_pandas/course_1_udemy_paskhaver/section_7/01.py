import pandas as pd

ds = pd.read_csv('../chicago.csv').dropna(how='all')

print(ds, ds.nunique())
print("------------------------------------")
print(ds.info())

ds["Department"] = ds["Department"].astype("category")

print(ds.info())