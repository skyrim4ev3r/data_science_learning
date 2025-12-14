import pandas as pd

foods = pd.read_csv("../restaurant_foods.csv", index_col="Food ID")
customers = pd.read_csv("../restaurant_customers.csv", index_col="ID")
week1 = pd.read_csv("../restaurant_week_1_sales.csv")
week2 = pd.read_csv("../restaurant_week_2_sales.csv")
#########
print(week1.merge(customers, how="left", left_on="Customer ID", right_index=True))
 ## cutomers use id for index, so no more right_on ==> instead right_index = True
 ###########

print(week1.merge(customers, how="left", left_on="Customer ID", right_index=True)
      .merge(foods, how="left", left_on="Food ID", right_index=True))
###############