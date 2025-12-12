import pandas as pd
import datetime as dt

emps = pd.read_csv("../employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
emps["Last Login Time"] = pd.to_datetime(emps["Last Login Time"], format="%H:%M %p").dt.time
emps["Senior Management"] = emps["Senior Management"].astype(bool)
emps["Gender"] = emps["Gender"].astype("category")

print(emps["First Name"].duplicated()) # first occurnes wont be count duplicate
print(emps[emps["First Name"].duplicated()])

filter1 = emps["First Name"].duplicated(keep="last") # "first" or "last" or False !!?
print(emps[filter1])

filter2 = emps["First Name"].duplicated(keep=False) # False mean keep just duplicates
print(emps[filter2])
print("-----------------------------------------------")
print(emps[~filter2])
print(emps.drop_duplicates(["First Name"], keep=False))
print("-----------------------------------------------")
print(emps.drop_duplicates("Team", keep="last")) # "first" or "last" or Fals
print(emps.drop_duplicates(subset=["Team"]))

print(emps.drop_duplicates(subset=["Senior Management", "Team"]).sort_values("Team"))
print("-----------------------------------------------")
print(emps["Gender"].unique())
print(type(emps["Gender"].unique()))
print(emps["Team"].unique())
print(type(emps["Team"].unique()))
print("-----------------------------------------------")
print(emps["Team"].nunique())
print(emps["Team"].nunique(dropna=True))
print(emps["Team"].nunique(dropna=False))
print("-----------------------------------------------")
print(emps.nunique())