import pandas as pd

ds = pd.read_csv("../jamesbond.csv", index_col="Film")
print(ds)

ds = pd.read_csv("../jamesbond.csv")
ds = ds.set_index("Film")
print(ds)
ds = ds.reset_index()
ds = ds.reset_index()
ds = ds.reset_index()
print(ds)
print("-----------")
ds["index"] = ds["index"] + 1
print(ds)
ds = ds.set_index("index")
ds = ds.set_index("level_0")
print(ds)
ds = ds.reset_index().set_index("Film")
print(ds)