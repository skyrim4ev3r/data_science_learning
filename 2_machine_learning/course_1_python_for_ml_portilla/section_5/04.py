import pandas as pd
import numpy as np

df = pd.read_csv('./ibm.csv')

print(df.sort_values(['High', 'Low'], ascending=[False, True]).head())
print(df['High'].max(), df['High'].idxmax())