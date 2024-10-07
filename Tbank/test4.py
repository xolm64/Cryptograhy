
import math


def is_simple_number(number):

    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))

    for element in divisors:
        if number % element == 0:
            return False
    return True

x = input()
y = x.split(" ")
not_simpl=[]
for z in range(int(y[0]), int(y[1])+1):
    if not is_simple_number(z) :
        not_simpl.append(z)

def get_delitel(num):
    delitel = []
    for i in range(1, num + 1):
        if num % i == 0 :
            delitel.append(i)
    return delitel


new_get_del=0

for n in not_simpl:
    b = get_delitel(n)

    if is_simple_number(len(b)):
        new_get_del=new_get_del+1


print( new_get_del)
