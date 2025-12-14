import pandas as pd
import datetime as dt

day = dt.date(2022, 1, 1)

print(day, day.day, day.year)
d = dt.datetime(2012, 11, 1)
print(d.hour)
d = dt.datetime(2012, 11, 1, 8)
d = dt.datetime(2012, 11, 1, 8, 45)
d = dt.datetime(2012, 11, 1, 8, 45, 1)

print(d.hour)
#######################################
## timestamp pd

ts = pd.Timestamp(2012, 11, 8)
print(ts)
ts = pd.Timestamp(2012, 11, 8, 8)
print(ts)
ts = pd.Timestamp(2012, 11, 8, 6 ,6, 59)
print(ts)

ts = pd.Timestamp("2012-12-01")
print(ts)
ts = pd.Timestamp("2012/12/01")
print(ts)
print(pd.Timestamp("2012-12-01 06:11:11"))

print(pd.Series([pd.Timestamp("2012-12-01 06:11:11")]).iloc[0])
print(pd.DatetimeIndex(["2025-01-01","2023-02-02"]))
print(pd.DatetimeIndex([ts, ts]))