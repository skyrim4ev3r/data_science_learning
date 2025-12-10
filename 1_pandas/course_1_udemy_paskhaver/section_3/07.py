import pandas as pd

pokemon = pd.read_csv("../pokemon.csv", index_col=["Name"]).squeeze("columns")

print(pokemon.value_counts())
print(pokemon.value_counts(ascending=True, normalize=True) * 100)

print('--------------------')

print(pokemon.apply(len)) # its function pass

def count_of_a(s):
    return s.count("a")

print(pokemon.apply(count_of_a))
print(pokemon.apply(lambda x: x.count("a")))