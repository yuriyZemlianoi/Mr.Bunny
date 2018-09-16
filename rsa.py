import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

def test():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate pub and priv key
    print('pk', key)
    publickey = key.publickey() # pub key export for exchange
    print('publickey', publickey)

    encrypted = publickey.encrypt('encrypt this message', 32)
    #message to encrypt is in the above line 'encrypt this message'

    print('encrypted message:', encrypted)
    #ciphertext

    #decrypted code below
    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
    print('decrypted', decrypted)