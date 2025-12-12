import pandas as pd

ds = pd.read_csv("../jamesbond.csv", index_col="Film").sort_index()

print(ds.sample())
print(ds.sample(n=5))
print(ds.sample(n=2, axis="columns"))

#highest values

print(ds.sort_values("Box Office", ascending=False).head(5))
print(ds.nlargest(n=4, columns="Box Office"))
print(ds["Box Office"].nlargest(n=4))

#lowest values
print(ds.sort_values("Box Office", ascending=True).head(5))
print(ds.nsmallest(n=4, columns="Box Office"))
print(ds["Box Office"].nsmallest(n=4))

filter1 = ds["Actor"] == "Sean Connery"
print(ds.loc[filter1])
print(ds.where(filter1))