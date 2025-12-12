import pandas as pd
import datetime as dt

emps = pd.read_csv("../employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
emps["Last Login Time"] = pd.to_datetime(emps["Last Login Time"], format="%H:%M %p").dt.time
emps["Senior Management"] = emps["Senior Management"].astype(bool)
emps["Gender"] = emps["Gender"].astype("category")

print(emps["Gender"] == "Male")

print(emps[emps["Gender"] == "Male"])
print(emps[emps["Gender"] != "Male"])

on_finance_team = emps["Team"] == "Finance"
print(emps[on_finance_team])

print(emps[emps["Senior Management"]]) # we changed dtype to true or false already

high_salary_emps = emps["Salary"] > 120000

print(emps[high_salary_emps])

print(emps[emps["Bonus %"] < 2])

old = emps["Start Date"] < "1985-01-01"

print(emps[old])

dt.time(12, 0, 0)

print(emps[emps["Last Login Time"] < dt.time(12, 0, 0)])