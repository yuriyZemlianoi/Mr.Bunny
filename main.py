import json
import time
import urllib.request
#import urllib2.urlopen
import redis
from lcd import *

from threading import Thread

count = 0
txLast = ''
uuid = ''
amount = 0

from bunny import *
from beep import *
from rsa import *

privateKey = "-----BEGIN RSA PRIVATE KEY-----MIIEpAIBAAKCAQEAjt8XQ3Mk5cEGHaGwBtO+bbVIFlCt3om2rPyGvvr3OzQMsLoL4MmEQKK507ayGh6jnPrxt3zxTQtXZrMZuYh9Lu5ZUMUkq2Dr4O1ePNWUZj6FuW8JMxwPIBXbnZ5fXCBN9EoMFHox7dm/FqQbfKuAqrlQuw2dBFNHbsoDj2xPaPDt7zuJp8Cn5pvySib2xRyyPwjFiZbQDtsGazH8GAeI5wow3zCEyMJawWr4JePNLLOpV2nF3uE1OVpHvYU6tIzPMCh/fiSDWohrFasKxV/+uPMgpPGeF8h8WP8SSPznrczk10R/6HTzP7j7Hy2IpEH+1mXaA7rv6Rlx6fumhK5jSwIDAQABAoIBAHPaxGqVvJ3y4Jq2up9OpWUhU8uEsPl8gv3T6RCFQmZn1sKYm3k08GHZkwbzZ4l2vwZVGB3K24G2aLGHGp0w6RJdhV/R/eJbPeuvkHOUXjprCNVODQ+8+SbzkptGCd4S9CPcx97zF/ngUOxzNzbpe/T1QVntuB4ByjM07Z4oHlzhiv5fgzvsInUBbyVanyhjf1x12Y/1TT35Cl4HN90UqNtWelsG4WQnLmezUnLVShHZigzljwqk41F0Wx7Z7xGWhTTBdUQ8rtYN+7GVp5TfdVeCyPv9tz2GtCubBJsLjwxT9IIyrFBdixDXB49Wjwybp5kTUyBrHuU9jv6nZARRvEECgYEA0k+5dLHbci7IDoMC7XsjZyWifTBndKrSJV8uMEN0nBkv60UXEB01GLPZAK2TZE1k9+5dQdI0dh0AtTs9YxpaMuODw9dpl/sy1sRDaEp673LMEumJPBQkmsPw1oYTE3AWKYPsC6zfHYBsnlIu3p33YUJuVvxi5QqFy6el//XWj5UCgYEArejBKKzBar0+HaCiTLbAGx8ANUiBB6xMqee+eokY2bCbPJ2Zr1jZWxt5QRWLp9h4EBB0ZF8MLGi7PbZlhorfJUgt/cqjFsBsgBaXVm9MwGTngQpCo8frAw9CfQN2NWSVPT32J2AvsiWkVxEPUeAqYOX1hrXO+GiYGWzjEV03718CgYEAw9DvQDQJuvrL0pcxNqSchgGIlT9oVDxohdtlShLElELvVwNxQdOwCFwMBJGY1p8pD5+kvRBXQFIowpVxxsBWk2M64DHFY3jEESuUB5qxdBlS4ZkH6iRnIKKnr1YOlN6cA/OM6CIBa5qTh6XFdglmt+v+iIdeHRv7D2/9I6FmMTECgYALxidVrqSFqnxLGzYBxZmp/GZSNS9vKo4iLqtptmB1VIyeBPmDsps8nNaPvnqvCWvPgp2usfSsCQcsPW4QNtS2vHVIqnByOOLfpSfn1S84E1zNErnCRuW1VlIlDpfxM3cbJ1fEALIZ+IxwzJnh7DBSUR9XWHXDwakSh5mz8kC4NwKBgQCR+f6hTGZsgKanC6U+hCrb1zh6CafkHkwhl6xVS+UFXBTvrGOhK1nDh/2YSWdv3ZWxB62Nhcq99r4W/cuzBZMe9eDdVzv6rKn1z7TIX7ULPg2M20A66HLA8LhBBPSNlJ37Dy7OXvlbnnCPbQZ6tEObrfToRT2hWoms/SJb9mJ3cQ==-----END RSA PRIVATE KEY-----";

node_user = '61bad923-4b87-4ef2-ad59-57e33eed5f71'
node_cash = 'c6d664fe-a4f4-41c0-afe3-c2c73a95b317'
url_base = 'http://104.248.47.57:2000/api/v1/nodes/'


from flask import Flask, request

app = Flask(__name__)
bunny = Bunny()

def build_url(node1):
    return url_base+node1+'/contractors/transactions/max/1/?contractor_uuid='+node_cash

@app.route('/')
def index():
    return 'uuid: '+str(bunny.uuid)+'\namount: '+str(bunny.amount)+'\ntxLast: '+str(bunny.txLast)

@app.route('/history')
def history():
    red = bunny.get_redis()
    result = bunny.get_history(red)
    return str(result)

@app.route('/amount/<string:cur>', methods=['GET'])
def amount(cur):
    r = urllib.request.urlopen(build_url(node_user)).read()
    data = json.loads(r.decode('utf-8'))
    time.sleep(5)
    red = redis.StrictRedis(host='104.248.47.57', port=6379, db=0)
    result = red.get(data['data']['response_uuid'])
    data = json.loads(result.decode('utf-8'))
    amount = data['data']['records'][0]['max_amount']
    return str(round(int(amount)/float(bunny.get_price(cur)), 8))



@app.route('/withdraw', methods=['POST'])
def withdraw():
    content = request.json
    id = bytearray.fromhex(content['uuid'])
    #print(content['uuid'])
    #print(request.json["uuid"])
    global privateKey
    #id = rsa_decrypt(content['uuid'], privateKey)
    print(rsa_decrypt(id, privateKey))
    if id == bunny.uuid:
        msg = screen('BANKOMAT SEND: ' + str(bunny.amount))
        beep()
        bunny.uuid = ''
        bunny.amount = ''
        return msg
    return 'You already got this money!'

if __name__ == '__main__':
    threadVolume = Thread(target=bunny.bunny_jump)
    threadVolume.daemon = True
    threadVolume.start()
    #bunny_jump()
    app.run(host='0.0.0.0')
