import pandas as pd

emps = pd.read_csv("../employees.csv")

print(emps.info())

emps["Start Date"] = pd.to_datetime(emps["Start Date"], format="%m/%d/%Y")
emps["Last Login Time"] = pd.to_datetime(emps["Last Login Time"], format="%H:%M %p").dt.time
emps["Senior Management"] = emps["Senior Management"].astype(bool)
emps["Gender"] = emps["Gender"].astype("category")

print(emps)

print(emps.info())

emps = pd.read_csv("../employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
emps["Last Login Time"] = pd.to_datetime(emps["Last Login Time"], format="%H:%M %p").dt.time
emps["Senior Management"] = emps["Senior Management"].astype(bool)
emps["Gender"] = emps["Gender"].astype("category")

print(emps)