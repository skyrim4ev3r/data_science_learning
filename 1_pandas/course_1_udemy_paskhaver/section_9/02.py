import pandas as pd

df = pd.read_csv("../fortune1000.csv", index_col="Rank").sort_index()

sectors = df.groupby("Sector")

print(sectors.agg({"Revenue": "sum", "Employees": "mean"})) ## diff func for each agg...

## 2 companies in each sector with most employess
def custom_func(sector):
    return sector.nlargest(2, "Employees")

print(sectors.apply(custom_func))