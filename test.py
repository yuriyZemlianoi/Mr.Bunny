# red = redis.StrictRedis(host='104.248.47.57', port=6379, db=0)
# result = red.get('0011b149-fefc-4b58-96eb-344a889dc1b7')
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