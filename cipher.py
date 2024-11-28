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

if __name__ == "__main__":
    secretKey = newKey()
    print(secretKey)