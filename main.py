import redis
import urllib.request
import json
from lcd import *
count = 0
txLast = ''
url_base = 'http://104.248.47.57:2000/api/v1/nodes/'

node_user = 'be01e47d-244b-44e8-b1c0-50b643b366fa'
node_cash = '58d27f4a-b15f-43d3-8300-36fd09e07e69'

def get_redis():
    return redis.StrictRedis(host='104.248.47.57', port=6379, db=0)

def build_url(type, node1, node2='', amount=0):
    url = ''
    if type == 'history':
        url = url_base+node1+'/history/transactions/payments/0/1000/1/'
    if type == 'transaction':
        if amount == 0:
            print('Write amount!')
        url = url_base+node1+'/contractors/'+node2+'/1/?amount='+amount
    return url

def check_transaction(tx, red):
    result = red.get(tx)
    result = json.loads(result.decode('utf-8'))
    if result['status'] == 200:
        print(result)
        return result['data']['transaction_uuid']
    else:
        return False

def get_max(array):
    inverse = [(value, key) for key, value in array.items()]
    return max(inverse)[1]

def get_last_transaction(txs):
    fullArray = {}
    for r in result['records']:
        fullArray[r['transaction_uuid']] = r['unix_timestamp_microseconds']
    return get_max(fullArray)

def get_history(red):
    r = urllib.request.urlopen(build_url('history', node_user)).read()
    data = json.loads(r.decode('utf-8'))
    result = red.get(data['data']['response_uuid'])
    result = json.loads(result.decode('utf-8'))
    if result['status'] == 200:
        return result['data']
    else:
        return False

def send_amount_by_txs(diff, records):
    for i in range(0, diff):
        screen('BANKOMAT SEND: ' + str(result['records'][i]['amount']))

red = get_redis()
while True:
    result = get_history(red)
    if result:
        if count == 0 and result['count'] != 0:
            print('First run!')
            count = result['count']
            txLast = get_last_transaction(result['records'])
        elif count != result['count']:
            send_amount_by_txs(result['count']-count, result['records'])

            count = result['count']
            txLast = get_last_transaction(result['records'])
    else:
        print('Fucking ERROR. Say your Money Bay!')






# red = redis.StrictRedis(host='104.248.47.57', port=6379, db=0)
# result = red.get('0011b149-fefc-4b58-96eb-344a889dc1b7')
# res = json.loads(result.decode('utf-8'))
# print(res)