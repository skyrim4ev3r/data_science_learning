import pandas as pd

url = "https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv"

df = pd.read_csv(url)
col_names = df.columns.tolist()[0].split(";")
for i in range(len(col_names)):
    col_names[i] = col_names[i].strip()
print(col_names)
df = df["Username; Identifier;First name;Last name"].str.split(";", expand=True)

df.columns = col_names

print(df.head(2))

print(df.to_csv())
df.to_csv("./test.csv")
df.to_csv("./test_without_index.csv", index=False)
df.to_csv("./test_with_selected_cols.csv", index=False, columns=["Username", "Identifier"])