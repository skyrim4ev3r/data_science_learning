import pandas as pd

df = pd.read_csv("../ibm.csv", parse_dates=["Date"], index_col="Date").sort_index()
x = df.index + pd.DateOffset(days=365)
print(x)
y = df.index - pd.DateOffset(days=5)
print(y)

r = pd.date_range(start="1991-04-12", end="2023-04-12", freq=pd.DateOffset(years=1))
print(df[df.index.isin(r)])

############
print(df.index + pd.tseries.offsets.MonthEnd())
print(df.index - pd.tseries.offsets.MonthEnd())