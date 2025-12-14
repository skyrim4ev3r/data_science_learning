import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../ibm.csv", parse_dates=["Date"], index_col=["Date"])

def rank(price):
    if price < 50:
        return "Poor"
    if price < 100:
        return "Not bad"
    return "Good"

df["Close"].apply(rank).value_counts().plot(kind="bar")
plt.show()
df["Close"].apply(rank).value_counts().plot(kind="barh")
plt.show()
df["Close"].apply(rank).value_counts().plot(kind="line")
plt.show()
df["Close"].apply(rank).value_counts().plot(kind="area")
plt.show()

avg = df["Close"].mean()

def rank2(price, avg):
    if price > avg:
        return "above avg"
    return "below avg"

df["Close"].apply(lambda row: rank2(row, avg)).value_counts().plot(kind="pie", legend=True)
plt.show()