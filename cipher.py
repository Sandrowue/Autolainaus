from cryptography.fernet import Fernet

def newKey() -> str:
    key = Fernet.generate_key()
    return key

def createChipher(key: str) -> object:
    cipher = Fernet(key)
    return cipher

def encrypt(cipher: object, plainText: str) -> str:
    cryptoText = cipher.encrypt(plainText)
    return cryptoText

def decrypt(cipher: object, cryptoText: str, byteMode=False) -> str:
    if byteMode == True:
        plainText = cipher.decrypt(cryptoText)
    else:
        plainText = cipher.decrypt(cryptoText).decode()
    return plainText

def encryptString(plainText: str, key=b'N4c4aAnEyqjpvIzXD9wZ7doo5V6WOUGi7xvyxBq3gSA=') -> bytes:
    cihperEngine = createChipher(key)
    byteForm = bytes(plainText, 'utf-8')
    cryptoText = encrypt(cihperEngine, byteForm)
    return cryptoText

def decryptString(cryptoText: bytes, key=b'N4c4aAnEyqjpvIzXD9wZ7doo5V6WOUGi7xvyxBq3gSA=') -> str:
    cipherEnginge = createChipher(key)
    plainText = str(decrypt(cipherEnginge, cryptoText))
    return plainText

if __name__ == "__main__":
    secretKey = newKey()
    print(secretKey)