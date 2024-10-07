#ДЗ: Написать функцию которая генерирует пароль с такими свойствами:
#1. Есть как минимум одна заглавная буква;
#2. Есть как минимум одна маленькая буква;
#3. Есть как минимум две цифры;
#4. Есть как минимум один символ('.', '+', etc.);
#5. Длина как минимум 8 элементов.
import string
from random import choice

def get_password():
    password= choice(string.ascii_uppercase)+choice(string.ascii_lowercase)+choice(string.octdigits)+choice(string.octdigits)
    password= password +choice(string.punctuation)+choice(string.ascii_uppercase)+choice(string.ascii_lowercase)+choice(string.octdigits)
    return password

print(get_password())

