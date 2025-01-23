import pytest

import cipher


keyword = cipher.newKey()
print(keyword)

test_cipher = cipher.createChipher(keyword)
print(test_cipher)

encryption = cipher.encrypt(test_cipher, b'Kukkaruukku')
print(encryption)

decryption = cipher.decrypt(test_cipher, encryption)
print(decryption)

def test_decryption():
    assert cipher.decrypt(test_cipher, encryption) == 'Kukkaruukku'

string_encryption = cipher.encryptString('Kastelukannu')
print(string_encryption)

def test_decryptString():
    assert cipher.decryptString(string_encryption) == 'Kastelukannu'