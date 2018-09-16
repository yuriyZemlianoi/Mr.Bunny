# import rsa
#
# def rsa_create():
#     (pubkey, privkey) = rsa.newkeys(512)
#     return [pubkey, privkey]
#
# # шифруем
# def rsa_encrypted(message, pubkey):
#     return rsa.encrypt(message, pubkey)
#
# # расшифровываем
# def rsa_decrypt(crypto, privkey):
#     return rsa.decrypt(crypto, privkey)

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


def rsa_decrypt(crypto, privkey):
    cipher_rsa = PKCS1_OAEP.new(privkey)
    session_key = cipher_rsa.decrypt(crypto)
    return session_key