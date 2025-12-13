import pandas as pd

df = pd.read_csv("../foods.csv")

print(df.head(2))

print(df.pivot_table(values="Spend", index="Gender")) # default is avg
print(df.pivot_table(values="Spend", index="Gender", aggfunc="mean"))

print(df.pivot_table(values="Spend", index="Gender", aggfunc="sum"))
print(df.pivot_table(values="Spend", index="Item", aggfunc="sum"))
print(df.pivot_table(values="Spend", index=["Gender", "Item"], aggfunc="sum"))
print(df.pivot_table(values="Spend", index=["Gender", "Item"], columns="City", aggfunc="sum"))
print("-----------------------------------------------------------------------")
print(df.pivot_table(values="Spend", index="Item", columns=["Gender", "City"], aggfunc="sum"))
print(df.pivot_table(values="Spend", index="Item", columns=["Gender", "City"], aggfunc="count"))
print(df.pivot_table(values="Spend", index="Item", columns=["Gender", "City"], aggfunc="max"))