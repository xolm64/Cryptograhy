

x = input()
password_leters = input()
len_password = int(input())

k = list(x)
spisok = []
for size in range(len(password_leters),len_password+1):

    y = len(k)-size

    for n in range(y+1):
        new_k = k[n:n+size]


        if set(password_leters) == set(new_k):
            spisok.append(new_k)

if len(spisok) == 0:
    print("-1")
else:
    spisok.sort(key=len)

    print("".join(spisok[-1]))








