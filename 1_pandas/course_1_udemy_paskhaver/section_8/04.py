import pandas as pd

ds = pd.read_csv("../worldstats.csv", index_col=["year", "country"]).sort_index()

print(ds)

print(ds.stack())
print(type(ds.stack()))

ds2 = ds.stack()
print("########################################################")
print(ds2.unstack())
print(ds2.unstack(level=1))
print(ds2.unstack(level="year"))
print(ds2.unstack(level=2))
print(ds2.unstack(level=-3))
print(ds2.unstack([1, 2]))
print(ds2.unstack(["country", "year"]))