
from bottle import route, run, template, request
import json, os

cfg = {
    'gy': '贵阳',
    'hz': '杭州',
    'sz': '深圳',
    'bj': '北京',
}

@route('/trend')
def go():
    topn = int(request.query['top'])
    loc = request.query['loc']
    reverse = int(request.query['sort'])
    jobj = {}
    with open('data/%s-prices.json' % loc, 'r') as fobj:
        jobj = json.load(fobj)
    dataobj = {}
    for k in jobj.keys():
        for k2 in jobj[k].keys():
            item = jobj[k][k2]
            if type(item) == type(jobj): dataobj[k2] = []
    for k in jobj.keys():
        for k2 in jobj[k].keys():
            item = jobj[k][k2]
            if type(item) == type(jobj): dataobj[k2].append(item["avg"])
    datastr = []
    for name in dataobj.keys():
        datastr.append({"name": name, "data": dataobj[name]})
    reverse = True if reverse == 1 else False
    datastr = sorted(datastr, key=lambda y: sum(y['data']) / len(y['data']), reverse=reverse)
    topn = 100 if topn == 0 else topn
    datastr = datastr[:topn]
    datastr = json.dumps(datastr)
    datastr = datastr.replace('"name"', 'name')
    datastr = datastr.replace('"data"', 'data')
    return template('html', pricesData=datastr, locname="'%s房价走势'" % cfg[loc])

run(host='localhost', port=8080, debug=True)
