import os
from keys import secret_key
from cryptography.fernet import Fernet

fernet_key =Fernet(secret_key)

list_decode_files = os.listdir('./decrypted_reports')

for file in list_decode_files:

    if file == "__init__.py":
       continue
    else:
        if 'c' not in file:
            with open(f'./decrypted_reports/{file}', 'r' ) as f:
                result = f.read()

            encrypted_file = fernet_key.encrypt(b'result').decode()

            with open(f'./encrypted_reports/{file}', 'w') as f:
                f.write(f'{encrypted_file}')

print('Все файлы в название которых нет буквы "с" зашифрованы и записаны в директорию encrypted_reports')