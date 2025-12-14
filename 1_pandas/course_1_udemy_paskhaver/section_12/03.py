import pandas as pd

url = "https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv"

df = pd.read_csv(url)
col_names = df.columns.tolist()[0].split(";")
for i in range(len(col_names)):
    col_names[i] = col_names[i].strip()

df = df["Username; Identifier;First name;Last name"].str.split(";", expand=True)

df.columns = col_names

with pd.ExcelWriter("./test.xlsx") as excel_file:
    df.to_excel(excel_file, sheet_name="1", index=False)
    df.to_excel(excel_file, sheet_name="another sheet", index=False, columns=["Username", "Identifier"])

data = pd.read_excel("./test.xlsx", sheet_name=None)
print(data)