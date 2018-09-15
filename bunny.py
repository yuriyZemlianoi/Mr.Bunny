import redis
import urllib.request
import json
import requests

class Bunny:


    url_base = 'http://104.248.47.57:2000/api/v1/nodes/'

    node_user = 'be01e47d-244b-44e8-b1c0-50b643b366fa'
    node_cash = '58d27f4a-b15f-43d3-8300-36fd09e07e69'

    def __init__(self):
        self.count = 0
        self.txLast = ''
        self.uuid = ''
        self.amount = 0

    def get_redis(self):
        return redis.StrictRedis(host='104.248.47.57', port=6379, db=0)

    def build_url(self, type, node1, node2='', amount=0):
        url = ''
        if type == 'history':
            url = self.url_base+node1+'/history/transactions/payments/0/1000/1/'
        if type == 'transaction':
            if amount == 0:
                print('Write amount!')
            url = self.url_base+node1+'/contractors/'+node2+'/transactions/1/?amount='+amount
        return url

    def check_transaction(self, tx, red):
        result = red.get(tx)
        result = json.loads(result.decode('utf-8'))
        if result['status'] == 200:
            print(result)
            return result['data']['transaction_uuid']
        else:
            return False

    def get_max(self, array):
        inverse = [(value, key) for key, value in array.items()]
        return max(inverse)[1]

    def get_last_transaction(self, txs):
        fullArray = {}
        for r in txs:
            fullArray[r['transaction_uuid']] = r['unix_timestamp_microseconds']
        return self.get_max(fullArray)

    def get_history(self, red):
        r = urllib.request.urlopen(self.build_url('history', self.node_user)).read()
        data = json.loads(r.decode('utf-8'))
        result = red.get(data['data']['response_uuid'])
        result = json.loads(result.decode('utf-8'))
        if result['status'] == 200:
            return result['data']
        else:
            return False

    def send_money_back(self, amount):
        r = requests.post(self.build_url('transaction', self.node_cash, self.node_user, amount))
        if r.status_code == 200:
            return True
        else:
            return False

    def send_amount_by_txs(self, diff, records):
        if self.uuid != '':
            for i in range(0, diff):
                self.send_money_back(records[i]['amount'])
            return False
        for i in range(0, diff):
            self.amount = records[i]['amount']
            self.uuid = records[i]['transaction_uuid']
        return True

    def bunny_jump(self):
        red = self.get_redis()
        while True:
            result = self.get_history(red)
            if result:
                if self.count == 0 and result['count'] != 0:
                    print('First run!')
                    self.count = result['count']
                    self.txLast = self.get_last_transaction(result['records'])
                elif self.count != result['count']:
                    self.send_amount_by_txs(result['count']-self.count, result['records'])
                    self.count = result['count']
                    self.txLast = self.get_last_transaction(result['records'])
            else:
                print('Fucking ERROR. Say your Money Bay!')