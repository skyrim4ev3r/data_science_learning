import pandas as pd

ds = pd.read_csv("../jamesbond.csv", index_col="Film").sort_index()

ds.rename(columns={"Year": "yy", "Actor": "aa"}, inplace=True)
ds.rename(index={"Casino Royale": "yy"}, inplace=True)
print(ds)
print(ds.columns)
ds.columns = ["1", "2", "3", "4", "5", "6"] # to replace entire cols names, same len
print(ds)

filter1 = ds["2"] == "Roger Moore"
ds.drop(columns=["3"], index=["Skyfall"], inplace=True)
print(ds)

ds.pop("1")
del ds["6"]
print(ds)