import pandas as pd

foods = pd.read_csv("../restaurant_foods.csv")
customers = pd.read_csv("../restaurant_customers.csv")
week1 = pd.read_csv("../restaurant_week_1_sales.csv")
week2 = pd.read_csv("../restaurant_week_2_sales.csv")

print(week1.merge(foods, how="left", on="Food ID"))

print(week2.merge(customers, how="left", left_on="Customer ID", right_on="ID"))

print(week2.merge(customers, how="left", left_on="Customer ID", right_on="ID").drop("ID", axis="columns"))

############

print(week1.merge(week2, how="inner", on="Customer ID"))
print(week1.merge(week2, how="inner", on="Customer ID", suffixes=["_week1", "_week2"]))

######### both weeks same food same customer
print(week1.merge(week2, how="inner", on=["Customer ID", "Food ID"]))

########## full-outer join
print(week1.merge(week2, how="outer", on="Customer ID"))
print("----------------")
print(week1.merge(week2, how="outer", on="Customer ID")
      .groupby("Customer ID")
      .filter(lambda x: len(x) > 1)
      #.groupby("Customer ID")
      #.first()
      )
res =week1.merge(week2, how="outer", on="Customer ID", indicator=True)
print(res)
print(res["_merge"].value_counts())

filter1 = res["_merge"].isin(["left_only", "right_only"])
print(res[filter1])
