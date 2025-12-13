import pandas as pd

ds = pd.read_csv('../chicago.csv', index_col="Name").dropna(how='all').sort_index()
ds.index = ds.index.str.strip().str.title()
ds.columns = ds.columns.str.upper()
print(ds)

print(ds["POSITION TITLE"].str.split(" ").str.get(0).value_counts())
##
ds = ds.reset_index()
print(ds["Name"].str.title().str.split(",").str.get(1).str.strip().str.split(" ").str.get(0).value_counts())
print(ds["Name"].str.title().str.split(",", expand=True))

ds[["Last Name", "First Name"]] = ds["Name"].str.title().str.split(",", expand=True)

print(ds)

print(ds["POSITION TITLE"].str.split(" ", expand=True))
print(ds["POSITION TITLE"].str.split(" ", expand=True, n=1))