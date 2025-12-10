import pandas as pd

pokemon = pd.read_csv("../pokemon.csv", index_col=["Name"]).squeeze("columns")

pokemon.iloc[0] ="test"
print(pokemon.head())
print('--------------------')
pokemon.iloc[[0, 2 ,4]] = ["test", "test2", "test"]
print(pokemon.head())
print('--------------------')

pokemon.loc[["Bulbasaur", "Ivysaur" ,"Venusaur"]] = ["test4", "test5", "test6"]
print(pokemon.head())