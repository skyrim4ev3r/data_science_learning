import pandas as pd

ds = pd.read_csv("../bigmac.csv", parse_dates=["Date"], date_format="%Y-%m-%d", index_col=["Date", "Country"]).sort_index()

print(ds.index.get_level_values("Date"))
print(ds.index.get_level_values(0))

print("------------------------")

ds.index.set_names(names="new_date", level=0, inplace=True)

print(ds.index)

ds.index.set_names(names=["new_date", "new_country"], inplace=True)

print(ds.index)

## sort is base on level0 then 1 then 2...

ds.sort_index(ascending=[True, False], inplace=True)

print(ds.head(2))
ds.sort_index(ascending=[True, True], inplace=True)

print(ds.head(2))
print("------------------------")

print(ds.iloc[0])
print(ds.loc["2000-04-1", "Price in US Dollars"]) #??
print(ds.loc["2000-04-1", "Canada"]) #?? both works??
print(ds.loc[("2000-04-1", "Canada")]) # use this for multi index for clearity
#print(ds.iloc[(1, 2)])
print(ds.loc[("2000-04-1", "Canada"):("2000-04-1", "Taiwan")])
