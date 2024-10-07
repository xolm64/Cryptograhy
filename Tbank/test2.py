

x = input(" введите количество дней ")
y = input("список замеров наблюдений ")

list_zamerov = y.split(" ")

condition_len = int(x) == len(list_zamerov)
conditioon_up = True
bez_minus_odin = [x for x in list_zamerov if x != '-1']
print(bez_minus_odin)
left1 = None
right1 = None
for i in range(len(bez_minus_odin)-1):
    left1 = int(bez_minus_odin[i])
    right1 = int(bez_minus_odin [i+1])
    print(left1, right1)
    if left1 > right1:
        conditioon_up = False
        break
if condition_len and conditioon_up:
    print('Yes')
else:
    print("No")

