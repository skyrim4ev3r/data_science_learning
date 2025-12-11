import pandas as pd

nba = pd.read_csv("../nba.csv")

print(nba.fillna(0))
nba["Salary"] = nba["Salary"].fillna(0).astype("Int32").astype("int").astype("float128").astype(int)
nba["College"] = nba["College"].fillna(value="Unknown")
print(nba, nba.dtypes)

print(nba["Team"].nunique())
print(nba.nunique())
print(nba.info())

nba["Position"] = nba["Position"].astype("category")
nba["Team"] = nba["Team"].astype("category")

print(nba["Team"].nunique())
print(nba.nunique())
print(nba.info())