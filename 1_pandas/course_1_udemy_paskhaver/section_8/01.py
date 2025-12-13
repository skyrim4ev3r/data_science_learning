import pandas as pd

ds = pd.read_csv("../bigmac.csv", parse_dates=["Date"], date_format="%Y-%m-%d")

print(ds)
print(ds.info())
print(ds.dtypes)

ds1 = ds.set_index(keys=["Date", "Country"]) # order matter
print(ds1)
ds2 = ds.set_index(keys=["Country", "Date"]).sort_index() # order matter
print(ds2)
print("--------------------------------------------------")
print(ds.nunique())

ds = pd.read_csv("../bigmac.csv", parse_dates=["Date"], date_format="%Y-%m-%d", index_col=["Date", "Country"]).sort_index()
print(ds)
print(ds.index)
print("--------------------------------------------------")
print(ds.index.names)
print(ds.index[0])
print(type(ds.index[0]))