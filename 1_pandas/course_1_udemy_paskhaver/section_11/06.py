import pandas as pd

print(pd.Timestamp("2023-01-01") - pd.Timestamp("2023-03-20"))
print(type(pd.Timestamp("2023-01-01") - pd.Timestamp("2023-03-20")))
print(pd.Timedelta("3 days 2 hours 1 second"))

df = pd.read_csv("../ecommerce.csv", index_col="ID", parse_dates=["order_date", "delivery_date"],
                 date_format="%m/%d/%y")

print(df.head(2))

print(df["delivery_date"] - df["order_date"])

df["DT"] = df["delivery_date"] - df["order_date"]

print(df)
df["twice long"] = df["delivery_date"] + df["DT"]
print(df)
print(df["DT"].max())