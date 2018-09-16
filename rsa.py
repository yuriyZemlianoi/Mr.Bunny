import rsa

def rsa_create():
    (pubkey, privkey) = rsa.newkeys(512)
    return [pubkey, privkey]

# шифруем
def rsa_encrypted(message, pubkey):
    return rsa.encrypt(message, pubkey)

# расшифровываем
def rsa_decrypt(crypto, privkey):
    return rsa.decrypt(crypto, privkey)