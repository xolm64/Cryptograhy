import pandas as pd

df = pd.read_csv('people.csv')

result_male = df[df['Gender'] == 'Male' ]
result_male.to_csv('result_male.cvs')

print(result_male)
