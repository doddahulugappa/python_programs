import pandas as pd

df = pd.read_csv('C:\\Users\\dodda\\Downloads\\transactions-2022-10-25.csv')

print(df.info)

df.dropna()
print(df.info)
print(df.describe())

print(df.columns)