import pandas as pd
import numpy as np

print(pd.options.display.min_rows, pd.options.display.max_rows, pd.options.display.max_columns)
print(pd.get_option("display.max_columns"))


pd.set_option("display.max_columns", 22)
print(pd.get_option("display.max_columns"))
print(pd.describe_option("display.max_columns"))
pd.reset_option("display.max_columns")
print(pd.describe_option("display.max_columns"))


pd.options.display.min_rows = 5
pd.options.display.max_rows = 10
pd.options.display.max_columns = 2

