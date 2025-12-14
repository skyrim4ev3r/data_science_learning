import pandas as pd

df = pd.read_csv("../ibm.csv", parse_dates=["Date"], index_col="Date").sort_index()

print(df.head())

print(df.iloc[300])
print(df.loc["2014-03-04"])
print("--------------------------------")
print(df.loc[pd.Timestamp(2014, 3, 4)])
print("--------------------------------")
print(df.loc["2014-03-04" : "2014-12-31"])
print("--------------------------------")
print(df.loc[pd.Timestamp(2014, 3, 4) : pd.Timestamp(2014, 12, 31)])
print("--------------------------------")

print(df.truncate(pd.Timestamp(2014, 3, 4), pd.Timestamp(2014, 12, 31)))

print(df.loc[pd.Timestamp(2014, 3, 4), "High" : "Close"])
print(df.loc[pd.Timestamp(2014, 3, 4), "Close"])