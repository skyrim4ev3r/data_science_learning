import pandas as pd

ds = pd.read_csv('../chicago.csv').dropna(how='all')
ds["Department"] = ds["Department"].astype("category")
ds["Position Title"] = ds["Position Title"].str.lower().str.rstrip() # strip is for space in l r
ds["Department"] = ds["Department"].str.strip().str.title().str.replace("Mgmnt", "Management")

print(ds["Department"].str.upper().str.len())
print(ds)
print(ds[ds["Position Title"].str.contains("water")])

ds2 = ds[ds["Position Title"].str.contains("water")]
print(ds2[ds2["Position Title"].str.startswith("fore")])
print("+++++++++++++++++++++++++++++++++")
filter2 = ds2["Position Title"].str.endswith("construction")
print(ds2[filter2])