import pandas as pd

nba = pd.read_csv("../nba.csv")

print(nba.Team)
print(nba["Team"]) # its view
print("-----------")
print(type(nba["Team"]))
print("-----------")
print(nba["Team"].iloc[0])
print("-----------")
team = nba["Team"]
team.iloc[0] = "test"
print("-----------")
print(nba["Team"].iloc[0])
print("-----------")
print(nba.head(2))

team = nba["Team"].copy()
team.iloc[0] = "new"
print("-----------")
print(nba["Team"].iloc[0])

nba.add