
def get_sum(a,b):
    return a+b

def get_pow(a,b):
    return  a**b

def print_start_and_end(func, *args):
    print('начало выполнения функции')
    result = func(*args)

    print('функция выполнена')
    return result

result = print_start_and_end(get_sum,5,6)

print(result)

result= print_start_and_end(get_pow, 3, 2)

print(result)