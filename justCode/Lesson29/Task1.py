import pandas as pd

df = pd.read_csv('data/sales.csv')

df['total price'] = df['Quantity'] * df['Price']

#print(df)

#result = df.groupby('Product')[['total price']].sum()
#print(result)


df['month'] = df['Date'].str[:7]
print(df)

result = df.groupby('month')[['total price']].sum()

print(result)