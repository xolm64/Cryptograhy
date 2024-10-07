
def reverse(list1):
    new_list = []
    for string in list1:
        new_string = string[::-1]
        new_list.append(new_string)
    return new_list

a = ["hello", "world"]

print(reverse(a))