import pandas as pd

ds = pd.read_csv("../salesmen.csv")
print(ds)

print(ds.pivot(index="Date", columns="Salesman", values="Revenue")) # tall to wide

ds = pd.read_csv("../quarters.csv")

print(ds.melt(id_vars="Salesman")) # wide to tall