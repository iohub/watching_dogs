# -*- coding: UTF-8 -*-

import requests, json
from datetime import date
import time
from bs4 import BeautifulSoup


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

def get_html(url):
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        raise Exception('get %d %s'% (r.status_code, url))
    return r.text

def get_price(html, result):
    soup = BeautifulSoup(html, features="html.parser")
    divs = soup.findAll("div", {"class": "info clear"})
    for item in divs:
        info = item.find('div', {'class': 'positionInfo'})
        district = info.find('a')
        if not district: continue
        name = district.text
        priceblock = item.find("div", {"class": "unitPrice"})
        price = priceblock.attrs['data-price']
        print('%s:%d' % (name, float(price)))
        if name not in result:
            result[name] = {'totalPrice': 0.0, 'total': 0 }
        result[name]['totalPrice'] += float(price)
        result[name]['total'] += 1


def get_district_price(baseurl):
    result = {}
    for page in range(1, 101):
        url = baseurl % page
        try:
            html = get_html(url)
            item = get_price(html, result)
        except Exception as e:
            print(e)
    return result


# baseurl = 'https://gy.ke.com/ershoufang/pg%dsf1a4a5/'
baseurl = 'https://sz.ke.com/ershoufang/pg%dsf1a3a4a5/'


if __name__ == '__main__':
    statics = {}
    result = get_district_price(baseurl)
    statics['ts'] = int(time.time())
    total = 0
    for name in result.keys():
        statics[name] = { 'avg': int(result[name]['totalPrice'] / result[name]['total']), 'total': result[name]['total']}
        total += result[name]['total']
    statics['total'] = total
    line = json.dumps(statics)
    prices = {}
    with open('data/sz-prices.json', 'r') as fobj:
        prices = json.load(fobj)
    prices[str(date.today())] = statics
    with open('data/sz-prices.json', 'w') as fobj:
        fobj.write(json.dumps(prices))
