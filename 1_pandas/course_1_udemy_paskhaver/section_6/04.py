import pandas as pd

ds = pd.read_csv("../jamesbond.csv", index_col="Film").sort_index()

#ds["Actor"].loc["Casino Royale"] = "gggg" #not good

ds.loc["Casino Royale", "Actor"] = "gggg"

print(ds)

ds["Actor"] = ds["Actor"].replace("gggg", "eeee")
print(ds)

filter1 = ds["Actor"] == "eeee"
ds.loc[filter1, "Actor"] = "qqqq"

print(ds)