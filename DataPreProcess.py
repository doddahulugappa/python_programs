import pandas as pd

df = pd.read_csv('data\\sample.txt')

print(df.info)

df.dropna()
print(df.info)
print(df.describe())

print(df.columns)