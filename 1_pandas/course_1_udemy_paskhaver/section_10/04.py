import pandas as pd

foods = pd.read_csv("../restaurant_foods.csv")
customers = pd.read_csv("../restaurant_customers.csv")
week1 = pd.read_csv("../restaurant_week_1_sales.csv")
week2 = pd.read_csv("../restaurant_week_2_sales.csv")

times = pd.read_csv("../restaurant_week_1_times.csv")

print(week1.merge(times, how="left", left_index=True, right_index=True))
print(week1.join(times)) ## when both are _index = True ==> shorter