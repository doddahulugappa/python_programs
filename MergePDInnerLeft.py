import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({
'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],

})

# DataFrame 2
df2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2'],
    'key': ['K0', 'K2', 'K3']
})

joined_df = df1.set_index('key').join(df2.set_index('key'), lsuffix='_df1', rsuffix='_df2')
print(joined_df)

isin_df = df1[df1['key'].isin(df2['key'])]
print(isin_df)

merged_df = df1.merge(df2, on='key', how='left')
print(merged_df)

merged_inner_df = df1.merge(df2, on='key', how='inner')
print(merged_inner_df)
