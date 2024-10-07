import pandas as pd


df_users = pd.read_csv("data/users.csv")

print(df_users.head(3))
print('++++++++++++++++++++++++++++++++++++')

df_posts = pd.read_csv("data/posts.csv")
print(df_posts.head(3))
print("+++++++++++++++++++++++++=result+++++++++++++++++++")
df_result = pd.merge(
    left = df_posts,
    right = df_users,
    on = ['user_id'],
    how = 'left'  # по дефолту Иннер, когда у обьединяет только пересечение таблиц
)

print(df_result.head(3))
df_result.to_csv('data/result.csv', index = False)  # индексом убрали слева нумерацию