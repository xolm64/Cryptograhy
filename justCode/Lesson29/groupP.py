import pandas as pd

df = pd.read_csv('data/sales.csv')


result = df.groupby('Product')[['Quantity' , 'Price']].sum()

print(result)