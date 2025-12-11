import pandas as pd

nba = pd.read_csv("../nba.csv")
nba["Salary"] = nba["Salary"].fillna(0).astype(int)
print(nba)

nba["Salary Rank"] = nba["Salary"].rank(ascending=False).astype(int)

print(nba.sort_values(by=["Salary"], ascending=False))