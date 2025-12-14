import pandas as pd

print(pd.date_range(start="2022-01-01", end="2022-01-06")) # default 1 day

print(pd.date_range(start="2022-01-01", end="2022-01-06", freq="2D"))

print(pd.date_range(start="2022-01-01", end="2023-01-06", freq="1M"))

print(pd.date_range(start="2022-01-01", end="2022-01-06", freq="B")) ## busines day ==? mon : fri
print(pd.date_range(start="2022-01-01", end="2023-01-06", freq="W")) ##week
print(pd.date_range(start="2022-01-01", end="2023-01-06", freq="W-FRI"))

print(pd.date_range(start="2022-01-01", end="2022-01-02", freq="3H"))
###############

print(pd.date_range(start="2022-01-01", freq="3H", periods=25))
print(pd.date_range(end="2022-01-01", freq="3H", periods=25))