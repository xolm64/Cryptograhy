x = str(input())


y  = x.split(",")
otvet = []

def func_raz(interval):
    x = interval.split('-')
    y = []
    for i in range(int(x[0]), int(x[-1])+1):
        y.append(i)
    return  y

for i in y:
    otvet.extend(func_raz(i))
otvet.sort()
z=[]
for i in otvet:
   z.append(str(i))

print(" ".join(z))

