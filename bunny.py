import redis
import urllib.request
import json
import requests
from kuna.client import KunaAPI

class Bunny:
    url_base = 'http://104.248.47.57:2000/api/v1/nodes/'
    node_user = 'be01e47d-244b-44e8-b1c0-50b643b366fa'
    node_cash = '58d27f4a-b15f-43d3-8300-36fd09e07e69'

    def __init__(self):
        self.count = 0
        self.txLast = ''
        self.uuid = ''
        self.amount = 0
        self.privateKey = "-----BEGIN RSA PRIVATE KEY-----MIIEpAIBAAKCAQEAjt8XQ3Mk5cEGHaGwBtO+bbVIFlCt3om2rPyGvvr3OzQMsLoL4MmEQKK507ayGh6jnPrxt3zxTQtXZrMZuYh9Lu5ZUMUkq2Dr4O1ePNWUZj6FuW8JMxwPIBXbnZ5fXCBN9EoMFHox7dm/FqQbfKuAqrlQuw2dBFNHbsoDj2xPaPDt7zuJp8Cn5pvySib2xRyyPwjFiZbQDtsGazH8GAeI5wow3zCEyMJawWr4JePNLLOpV2nF3uE1OVpHvYU6tIzPMCh/fiSDWohrFasKxV/+uPMgpPGeF8h8WP8SSPznrczk10R/6HTzP7j7Hy2IpEH+1mXaA7rv6Rlx6fumhK5jSwIDAQABAoIBAHPaxGqVvJ3y4Jq2up9OpWUhU8uEsPl8gv3T6RCFQmZn1sKYm3k08GHZkwbzZ4l2vwZVGB3K24G2aLGHGp0w6RJdhV/R/eJbPeuvkHOUXjprCNVODQ+8+SbzkptGCd4S9CPcx97zF/ngUOxzNzbpe/T1QVntuB4ByjM07Z4oHlzhiv5fgzvsInUBbyVanyhjf1x12Y/1TT35Cl4HN90UqNtWelsG4WQnLmezUnLVShHZigzljwqk41F0Wx7Z7xGWhTTBdUQ8rtYN+7GVp5TfdVeCyPv9tz2GtCubBJsLjwxT9IIyrFBdixDXB49Wjwybp5kTUyBrHuU9jv6nZARRvEECgYEA0k+5dLHbci7IDoMC7XsjZyWifTBndKrSJV8uMEN0nBkv60UXEB01GLPZAK2TZE1k9+5dQdI0dh0AtTs9YxpaMuODw9dpl/sy1sRDaEp673LMEumJPBQkmsPw1oYTE3AWKYPsC6zfHYBsnlIu3p33YUJuVvxi5QqFy6el//XWj5UCgYEArejBKKzBar0+HaCiTLbAGx8ANUiBB6xMqee+eokY2bCbPJ2Zr1jZWxt5QRWLp9h4EBB0ZF8MLGi7PbZlhorfJUgt/cqjFsBsgBaXVm9MwGTngQpCo8frAw9CfQN2NWSVPT32J2AvsiWkVxEPUeAqYOX1hrXO+GiYGWzjEV03718CgYEAw9DvQDQJuvrL0pcxNqSchgGIlT9oVDxohdtlShLElELvVwNxQdOwCFwMBJGY1p8pD5+kvRBXQFIowpVxxsBWk2M64DHFY3jEESuUB5qxdBlS4ZkH6iRnIKKnr1YOlN6cA/OM6CIBa5qTh6XFdglmt+v+iIdeHRv7D2/9I6FmMTECgYALxidVrqSFqnxLGzYBxZmp/GZSNS9vKo4iLqtptmB1VIyeBPmDsps8nNaPvnqvCWvPgp2usfSsCQcsPW4QNtS2vHVIqnByOOLfpSfn1S84E1zNErnCRuW1VlIlDpfxM3cbJ1fEALIZ+IxwzJnh7DBSUR9XWHXDwakSh5mz8kC4NwKBgQCR+f6hTGZsgKanC6U+hCrb1zh6CafkHkwhl6xVS+UFXBTvrGOhK1nDh/2YSWdv3ZWxB62Nhcq99r4W/cuzBZMe9eDdVzv6rKn1z7TIX7ULPg2M20A66HLA8LhBBPSNlJ37Dy7OXvlbnnCPbQZ6tEObrfToRT2hWoms/SJb9mJ3cQ==-----END RSA PRIVATE KEY-----";

    def get_price(self, cur):
        clientFirst = KunaAPI('test', 'test')
        ticker = clientFirst.get_recent_market_data(cur)['ticker']
        return (float(ticker['low'])+float(ticker['high'])+float(ticker['last']))/3

    def withdraw_kuna(self, access_key, secret_key):
        clientFirst = KunaAPI(access_key, secret_key)
        ticker = clientFirst.get_recent_market_data(cur)['ticker']

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