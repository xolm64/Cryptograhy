#  фильтрует список по нашей лямбде

num1 = [1,2,3,46,7]

num2 = list(filter(lambda x: x > 3 , num1))

print(num2)


def bol_3(x):
    if x > 3:
        return  x



def custom(l, func):
    x=[]
    for elem in l:
        func(elem)
        x = l.append(elem)
    return x

print(custom(num1, bol_3))

