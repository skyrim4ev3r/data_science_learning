import pandas as pd
import datetime as dt

emps = pd.read_csv("../employees.csv", parse_dates=["Start Date"], date_format="%m/%d/%Y")
emps["Last Login Time"] = pd.to_datetime(emps["Last Login Time"], format="%H:%M %p").dt.time
emps["Senior Management"] = emps["Senior Management"].astype(bool)
emps["Gender"] = emps["Gender"].astype("category")

is_female = emps["Gender"] == "Female"
is_in_marketing = emps["Team"] == "Marketing"

both_conditions = is_female &  is_in_marketing
one_condition =  is_female |  is_in_marketing

print(emps[both_conditions])
print(emps[one_condition])

xor_condition =  is_female ^ is_in_marketing

print(emps[xor_condition])

not_both_conditions = ~(is_female &  is_in_marketing)

print(emps[not_both_conditions])

triple_condition = is_female &  is_in_marketing & (emps["Salary"] > 100_000)
print(emps[triple_condition])