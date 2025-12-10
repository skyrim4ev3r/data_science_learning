import pandas as pd

pokemon = pd.read_csv("../pokemon.csv", index_col=["Name"]).squeeze("columns")

attack_powers = {
    "Grass": 10,
    "Water": 20,
    "Fire": 30
}

print(pokemon.map(attack_powers).sort_values()) # because of missed values it use float

attack_powers = pd.Series({
    "Grass": 10,
    "Water": 20,
    "Fire": 30
})

print(pokemon.map(attack_powers).sort_values())