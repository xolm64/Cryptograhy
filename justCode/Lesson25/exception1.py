# работа с ошибка и исключениями
print("начало")
a = "hello"

try:
    a_int= int(a)

except Exception as error:
    print(" вышла ошибка")
    print(error)
else:
    print('если не было ошибок') # можно не использовать , потому что в трай все выполняется
finally:
    print("выходим из трай эксепт. файнали выполняется всегда")

print('конец')

