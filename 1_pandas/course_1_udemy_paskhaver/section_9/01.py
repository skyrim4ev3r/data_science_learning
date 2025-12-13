import pandas as pd

df = pd.read_csv("../fortune1000.csv", index_col="Rank").sort_index()

print(df.head(2))

filter1 = df["Sector"] == "Retailing"

print(df[filter1]["Revenue"].sum()) ## need to do it for every sctor

sectors = df.groupby("Sector")
print(sectors)
print(len(sectors))
print(sectors.size())
print("---------------------------")
print(sectors.first())
print("---------------------------")
print(sectors.last())
print("---------------------------")
print(sectors.get_group("Energy"))
print("---------------------------")

print(sectors["Revenue"])
print(sectors["Revenue"].sum()) ## all at same time
print(sectors["Employees"].sum())

print(sectors[["Revenue", "Employees"]].sum())
print("---------------------------")
print("---------------------------")
sectors = df.groupby(["Sector", "Industry"])
print(sectors.first())
print(sectors.size())
print(sectors["Revenue"].sum().head(5))