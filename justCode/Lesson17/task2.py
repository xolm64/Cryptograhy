def get_square(x):
    return x ** 2


def get_cube(x):
    return x ** 3

def get_plus_3(list):
    list1 = []
    for elem in list:
        list1.append(elem + 3)
    return list1

def get_changed_list(l, func):         # функция высшего порядка MAP
    changed_numbers = []
    for elem in l:
        changed_number = func(elem)
        changed_numbers.append(changed_number)

    return changed_numbers


numbers = [7, 3, 12, 6]
squared_numbers = get_changed_list(numbers, get_square)
tripled_numbers = get_changed_list(numbers, get_cube)
plus_3 = get_plus_3(numbers)
plus_4 = get_changed_list(numbers, lambda x: x + 4) # вариант написания лямбы, чтобы не тратить строки на новые функции

print(squared_numbers)
print(tripled_numbers)
print(plus_3)
print(plus_4)