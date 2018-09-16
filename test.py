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

from rsa import *

test()