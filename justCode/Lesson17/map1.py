

numbers = [1,3,12,6]

def get_sq(list):
    sq_numbers=[]
    for elem in list:
        sq_numbers.append(elem ** 2)
    return sq_numbers


sq_numbers=get_sq(numbers)
print(sq_numbers)

