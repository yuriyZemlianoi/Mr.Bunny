import json
import time
import urllib.request
import redis
from lcd import *

from threading import Thread

count = 0
txLast = ''
uuid = ''
amount = 0

from bunny import *
from beep import *



node_user = 'be01e47d-244b-44e8-b1c0-50b643b366fa'
node_cash = '58d27f4a-b15f-43d3-8300-36fd09e07e69'
url_base = 'http://104.248.47.57:2000/api/v1/nodes/'


from flask import Flask

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



@app.route('/withdraw/<string:id>', methods=['GET'])
def withdraw(id):
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
