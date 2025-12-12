import pandas as pd
import datetime as dt

emps = pd.read_csv("../employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
emps["Last Login Time"] = pd.to_datetime(emps["Last Login Time"], format="%H:%M %p").dt.time
emps["Senior Management"] = emps["Senior Management"].astype(bool)
emps["Gender"] = emps["Gender"].astype("category")

filter1 = emps["Team"].isin(["Legal", "Sales", "Product"])
filter2 = (emps["Team"] == "Legal") |  (emps["Team"] == "Sales") | (emps["Team"] == "Product")
print(emps[filter1])
print(emps[filter2])

#############
print(emps[emps["Team"].isnull()])
print(emps[~emps["Team"].notnull()])
print(emps[emps["Team"].notnull()])

########## between

filter3 = (emps["Salary"] >= 50_000) & (emps["Salary"] <= 80_000)
filter4 = emps["Salary"].between(50_000, 80_000)
print(emps[filter3])
print(emps[filter4])

filter5 = emps["Bonus %"].between(2.0, 5.0)
print(emps[filter5])

filter6 = emps["Start Date"].between("1991-01-01", "2000-01-01")
print(emps[filter6])

filter7 = emps["Last Login Time"].between(dt.time(8, 30), dt.time(12, 0))
print(emps[filter7])