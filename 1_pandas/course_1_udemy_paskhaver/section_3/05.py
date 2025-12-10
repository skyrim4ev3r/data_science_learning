import pandas as pd

pokemon_df = pd.read_csv("../pokemon.csv", usecols=["Name"])

pokemon_series = pokemon_df.squeeze("columns")
pokemon_series.iloc[0] = "test" #ITS VIEW
print(pokemon_df.iloc[0])

print("-------------------")

pokemon_series = pokemon_df.squeeze("columns").copy()
pokemon_series.iloc[0] = "new_test"
print(pokemon_df.iloc[0])

print("-------------------")

google = pd.read_csv("../google_stock_price.csv", usecols=["Price"]).squeeze("columns")
print(google.count(), google.size) # count() dont include missed values
print(google.sum(), google.product(), google.mean(), google.max(), google.mean(), google.mode())
print("-------------------")
print(google.describe())