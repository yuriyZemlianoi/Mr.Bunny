# import json
#
# import redis
#
# red = redis.StrictRedis(host='104.248.47.57', port=6379, db=0)
# result = red.get('6f0cb703-8c0f-4f16-9cc1-e5962a4366af')
# res = json.loads(result.decode('utf-8'))
# print(res)

# from kuna.client import KunaAPI
#
# clientFirst = KunaAPI('test' 'test')
# ticker = clientFirst.get_recent_market_data('remuah')['ticker']
# print(ticker)
# ticker = clientFirst.get_recent_market_data('btcuah')['ticker']
# print(ticker)
# ticker = clientFirst.get_recent_market_data('ethuah')['ticker']
# print(ticker)

import os
import base64
from M2Crypto import RSA  # $ pip install m2crypto

# ssh-keygen -f ~/.ssh/id_rsa.pub -e -m PKCS8 >id_rsa.pub.pem
rsa = RSA.load_pub_key('id_rsa.pub.pem')     # load public key
encrypted = rsa.public_encrypt(b'hello world', RSA.pkcs1_oaep_padding)  # encrypt
print(base64.b64encode(encrypted).decode())

rsa = RSA.load_key(os.path.expanduser('~/.ssh/id_rsa'))  # load private key
encrypted = base64.b64decode(encrypted_base64)  # get raw bytes
print(rsa.private_decrypt(encrypted, RSA.pkcs1_oaep_padding).decode())  # decrypt