import pandas as pd

nba = pd.read_csv("../nba.csv")
##sort each col
print(nba["Name"].sort_values())

## sort_by
print(nba.sort_values("Name"))
print(nba.sort_values(by="Name", ascending=False, na_position="first"))
print(nba.sort_values(by=["Team", "Name"], ascending=False, na_position="first"))
print(nba.sort_values(by=["Team", "Name"], ascending=[True, False], na_position="first"))

new_nba = nba.sort_values(by=["Team", "Name"])
print(new_nba.sort_index()) # will be sorted by index no matter if it be int or str or date
print(new_nba.sort_index(ascending=False))