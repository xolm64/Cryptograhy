import pandas as pd

#df = pd.read_csv('data/sales.csv')


data = {
    "a": [1,2,99],
    'b': [4,3,5]
}

df = pd.DataFrame(data)
print(df)

df['result'] = df["a"] + df['b']

print(df)