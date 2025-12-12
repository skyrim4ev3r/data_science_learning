import pandas as pd

ds = pd.read_csv("../jamesbond.csv", index_col="Film").sort_index()

print(ds.loc["Thunderball"])
print("------------------")
print(ds.loc["Thunderball", "Year"])
print("------------------")
print(ds.loc[["Thunderball", "Casino Royale"], ["Year", "Actor"]])
print(ds.loc[["Thunderball", "Casino Royale"], "Year":])
print("------------------")
print(ds.loc[["Thunderball", "Casino Royale"]][["Year", "Actor"]])
print("------------------")
print(ds.loc[["Thunderball", "Casino Royale"]]["Year"])
print("------------------")
print(ds.iloc[0, 1])

