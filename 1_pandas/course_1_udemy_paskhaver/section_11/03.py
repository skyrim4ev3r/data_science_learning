import pandas as pd

ds = pd.Series(pd.date_range(start="2022-01-01", end="2023-01-06", freq="24D 3h"))
print(ds.dt.day)
print(ds.dt.month)
print(ds.dt.day_of_year)
print(ds.dt.day_name())
print(ds.dt.is_month_end, ds.dt.is_month_start)