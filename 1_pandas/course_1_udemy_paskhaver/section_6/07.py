import pandas as pd

ds = pd.read_csv("../jamesbond.csv", index_col="Film").sort_index()

print(ds["Actor"].apply(len))
print("----------------------   ")
def rank_movie(row):
    #print(row)
    year = row.loc["Year"]
    actor = row.loc["Actor"]

    if year >= 1980 and year < 1990:
        return "eeeee"

    return "tttt"

print(ds.apply(rank_movie, axis="columns"))

print(ds)