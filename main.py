#import json
#import time
#import urllib.request
#import urllib2.urlopen
#import redis
from lcd import *

from threading import Thread

count = 0
txLast = ''
uuid = ''
amount = 0

from bunny import *
#from beep import *
#from rsa import *

# node_user = '61bad923-4b87-4ef2-ad59-57e33eed5f71'
# node_cash = 'c6d664fe-a4f4-41c0-afe3-c2c73a95b317'
#url_base = 'http://104.248.47.57:2000/api/v1/nodes/'


from flask import Flask, request

app = Flask(__name__)
bunny = Bunny()

def build_url(node1):
    return bunny.url_base+node1+'/contractors/transactions/max/1/?contractor_uuid='+bunny.node_cash

@app.route('/')
def index():
    return 'uuid: '+str(bunny.uuid)+'\namount: '+str(bunny.amount)+'\ntxLast: '+str(bunny.txLast)

@app.route('/history')
def history():
    red = bunny.get_redis()
    result = bunny.get_history(red)
    return str(result)

@app.route('/amount/<string:cur>', methods=['GET'])
def amount(cur=''):
    r = urllib.request.urlopen(build_url(bunny.node_user)).read()
    data = json.loads(r.decode('utf-8'))
    time.sleep(5)
    red = redis.StrictRedis(host='104.248.47.57', port=6379, db=0)
    result = red.get(data['data']['response_uuid'])
    data = json.loads(result.decode('utf-8'))
    amount = data['data']['records'][0]['max_amount']
    if cur == '':
        return int(amount)
    return str(round(int(amount)/float(bunny.get_price(cur)), 8))

# @app.route('/tx/<string:tx>', methods=['GET'])
# def tx(tx):
#     red = redis.StrictRedis(host='104.248.47.57', port=6379, db=0)
#     result = red.get(tx)
#     data = json.loads(result.decode('utf-8'))

@app.route('/withdraw', methods=['POST'])
def withdraw():
    content = request.json
    id = content['uuid']
    print('get: ', id)
    print('was: ', bunny.uuid)
    if str(id) == str(bunny.uuid):
        return 'You already got this money!'
    else:
        msg = screen('BANKOMAT SEND: ' + str(bunny.amount))
        bunny.uuid = ''
        bunny.amount = ''
        return msg



if __name__ == '__main__':
    threadVolume = Thread(target=bunny.bunny_jump)
    #threadVolume.daemon = True
    threadVolume.start()

    app.run(host='0.0.0.0')
