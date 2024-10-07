from cryptography.fernet import Fernet

secret_key = Fernet.generate_key()
print(f'secret key {secret_key}')

fernet_key = Fernet(secret_key)

data = b"hello world"


encrypted_data = fernet_key.encrypt(data)

print(f"зашифрованный хелло ворлд {encrypted_data}")

