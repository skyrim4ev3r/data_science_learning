import pandas as pd

foods = pd.read_csv("../restaurant_foods.csv")
customers = pd.read_csv("../restaurant_customers.csv")
week1 = pd.read_csv("../restaurant_week_1_sales.csv")
week2 = pd.read_csv("../restaurant_week_2_sales.csv")

print(foods.head(2))
print("-----------------------")
print(pd.concat([week1, week2, foods]).sort_index()) # res index isnt unique aftewr this
print(pd.concat([week1, week2, foods], ignore_index=True)) # now res has unique index
print("-----------------------")
print(pd.concat([week1, week2, foods], keys=["Week 1", "Week 2", "FOOD"]).sort_index())
print("-----------------------")

df1 = pd.DataFrame([1, 2, 3], columns=["A"])
df2 = pd.DataFrame([1, 2, 3], columns=["B"])

print(pd.concat([df1, df2]))
print("-----------------------")
print(pd.concat([df1, df2], axis="columns")) # same index...