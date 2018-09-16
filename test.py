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

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))
