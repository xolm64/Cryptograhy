import pandas as pd

df = pd.read_csv('data/sales.csv')


result = df.groupby('Category').agg(
    {
        "Price": 'mean',
        'Quantity': "sum"

    }
)

print(result)


res =