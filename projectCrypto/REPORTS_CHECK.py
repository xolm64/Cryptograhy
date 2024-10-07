import os

list_decode_files = os.listdir('./decrypted_reports')

for file in list_decode_files:
    if file == '__init__.py':
        continue
    else:
        print(f"=========Читаем файл {file} до изменения=============")
        with open(f"./decrypted_reports/{file}", 'r') as f:
            file_read = f.read()
            print(file_read)
        print(f'======Читаем файл {file} после изменения "вра" на "дру"===========\n')
        result = file_read.replace('Вра', 'Дру')
        result = result.replace('вра', 'дру')
        print(result + ' Проверено!' )

