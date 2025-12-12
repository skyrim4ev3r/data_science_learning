import pandas as pd

ds = pd.read_csv("../jamesbond.csv")
print(ds.iloc[5])
print(ds.iloc[[1, 2, 3 ,5]])
print(ds.iloc[4:8])
print(ds.iloc[range(1, 10)])

ds = ds.set_index("Film")

print(ds.loc["Goldfinger"])
print(ds.loc["Casino Royale"])
#print(ds.loc["500"])
print(ds.loc[["Casino Royale", "Goldfinger"]])

#print(ds.loc["Goldfinger" : "Casino Royale"]) # error duplicate Casino..
print(ds.loc["Goldfinger" : "Moonraker"]) # "Moonraker" is included!!
print('-----------------------')
print(ds.loc["Moonraker" : "Goldfinger"]) ## order matter
print(ds.loc["Moonraker":])
print(ds.loc[:"Moonraker"])