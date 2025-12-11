import pandas as pd

nba = pd.read_csv("../nba.csv")

print(nba[["Name", "Team"]]) # here its copy
print(nba[["Team", "Name", "Team"]])

col_to_select = ["Team", "Name", "Team"]
print(nba[col_to_select])
print("--------------------")

nba["Sport"] = "test"
nba.insert(loc=3, column="New_sport", value="new_test")
nba["Salary_x2"] = nba["Salary"] * 2
nba.insert(loc=3, column="Salary_x2_new", value=nba["Salary"] * 2)

print(nba)
print("--------------------")
print(nba["Team"].value_counts())
print(nba["Position"].value_counts(normalize=True) * 100)
print(nba["Salary"].value_counts())
print("--------------------")

nba = pd.read_csv("../nba.csv")
print(nba.dropna()) # any rows with any missisg value
print(nba.dropna(how="any"))

print(nba.dropna(how="all")) # any rows witll all missing value
nba.at[591, "Name"] = "new"

print(nba.dropna(subset=["Name", "Salary", "College", "Height"], how="any"))