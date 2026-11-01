import pandas as pd

df = pd.read_csv("data/customer_support.csv")

print(df.head())
print(df.columns)
print(df.shape)
print(df.info())