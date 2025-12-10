import pandas as pd

pokemon = pd.read_csv("../pokemon.csv", index_col=["Name"]).squeeze("columns")
print(pokemon.sort_index())


pokemon = pd.read_csv("../pokemon.csv", usecols=["Name"]).squeeze("columns")
print(pokemon.iloc[0])
print(pokemon.iloc[[0, 10, 100]])

print(pokemon.iloc[-1 : -5 : -1])

print("-------------------")
pokemon = pd.read_csv("../pokemon.csv", index_col=["Name"]).squeeze("columns")
print(pokemon.loc["Bulbasaur"])
print(pokemon.iloc[0])
##print(pokemon["Bulbasaur"]) deprecated
##print(pokemon[0]) deprecated
print("------------------")
print(pokemon.get("Bulbasaur"))
print(pokemon.get("ttt", "404 not found"))
print(pokemon.get(["Bulbasaur", "ttt"], "404 not found"))
print(pokemon.get(["Bulbasaur", "ttt"]))
##print(pokemon.get(0)) ##deprecated

