import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../ibm.csv", parse_dates=["Date"], index_col=["Date"])

df.plot()
plt.show()

df.plot(y="Close")
plt.show()

df["Close"].plot()
plt.show()

##
print(plt.style.available)
plt.style.use("fivethirtyeight") # its global setting
df["Close"].plot()
plt.show()

plt.style.use("seaborn-v0_8-darkgrid")
df["Close"].plot()
plt.show()

###
