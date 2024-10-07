def second_max(numbers):
    numbers.sort()
    if len(numbers) < 2:
        return 'в списке менее двух чисел'
    else:
        return numbers[-2]


l= [1]
l2 = [1,5,4,3]

print(second_max(l))
print(second_max(l2))