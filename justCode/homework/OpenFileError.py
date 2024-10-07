

try:
    files = open('sdfsdf.txt', 'r')


except FileNotFoundError as error:
    print(f' ошибка открытия  файла {error}')
else:
    print('файл успешно открыт')

finally:
    s = "выходим из блока обработки ошибки"
    print("="*len(s))
    print(s)
    print("=" * len(s))

