import pandas as pd

ds = pd.read_csv("../bigmac.csv", parse_dates=["Date"], date_format="%Y-%m-%d", index_col=["Date", "Country"]).sort_index()


start = ("2018-01-01", "China")
end = ("2018-01-01", "Denmark")

print(ds.loc[start : end])
print("---------------------------")
print(ds.loc[start : end].transpose())
print("---------------------------")