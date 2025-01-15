import random

import requests
from bs4 import BeautifulSoup

Crypto_list = {
    'btc': 'bit',
    'ton': 'ton'
}


def get_crypto(crypto=None):
    if crypto is None:
        return 'Crypto not found'
    if crypto not in Crypto_list.keys(): return ('Something went wrong')
    page = requests.get(f'https://www.binance.com/en/price/{Crypto_list[crypto]}coin')
    if page.status_code != 200: return ('No page response')
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.findAll('meta')[2].get('content')
    price = text.split(' ')[5]
    return (price)


