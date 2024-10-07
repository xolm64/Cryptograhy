from cryptography.fernet import Fernet

secret_key = b'3-hPwgWK5QrCn9MEFHsvOzHsNSeP6ZFmFzBNHPxdrQA='

encrypted_data = b'gAAAAABnAVWFk7BWH-AqSoIN9w9eCVVsnqIBr6wgSKgrerntJc4Mi_9hj_OaFCOoDAECFsCZkiv-vGsyVDqd7XbZ1rC9Kqumhg=='

fernet_key= Fernet(secret_key)

dec_data = fernet_key.decrypt(encrypted_data)

print(dec_data.decode())  # можно и без декода, но тогда будет Б перед строчкой  , потому что работает с байтами