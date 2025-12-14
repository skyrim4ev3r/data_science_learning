# Excel files

# pip install openpyxl

import pandas as pd

data = pd.read_excel("../Data - Single Worksheet.xlsx")

print(data)

data = pd.read_excel("../Data - Multiple Worksheets.xlsx") ## default imports only first work sheet

print(data)

data = pd.read_excel("../Data - Multiple Worksheets.xlsx", sheet_name="Data 2")
print(data)
data = pd.read_excel("../Data - Multiple Worksheets.xlsx", sheet_name=1) # 0 index
print(data)

data = pd.read_excel("../Data - Multiple Worksheets.xlsx", sheet_name=["Data 1", "Data 2"]) # return hashmap
print(data)

data = pd.read_excel("../Data - Multiple Worksheets.xlsx", sheet_name=None) # None to get all
print(data)

print(data["Data 1"]["First Name"])