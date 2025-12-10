# csv comma seperated values
import pandas as pd
pokemon = pd.read_csv(filepath_or_buffer="../pokemon.csv", usecols=["Name"]).squeeze("columns")
#print(pokemon)
google = pd.read_csv(filepath_or_buffer="../google_stock_price.csv", usecols=["Price"]).squeeze("columns")
#print(google)

#print(pokemon.head()) #default 5
#print(pokemon.head(5))
#print(pokemon.head(n=5))
#print(google.tail(7))

#print(len(pokemon), type(pokemon), list(pokemon), sorted(pokemon))
#print(dict(pokemon))

print(max(google), min(google))

print("Bulbasaur" in pokemon)
print("Bulbasaur" in pokemon.index)

print("Bulbasaur" in pokemon.values)

print(google.sort_values(ascending=False))
print(google)
print(google.sort_values(ascending=True).head(3))