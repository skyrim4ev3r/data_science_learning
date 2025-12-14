import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 5))

print(df)

pd.options.display.precision = 20

print(df)