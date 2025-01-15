import time
import requests
from bs4 import BeautifulSoup

Crypto_list = {
    'btc': 'bitcoin',
    'ton': 'toncoin',
    'eth': 'ethereum',
    'bnb': 'bnb',
    'ada': 'cardano',
    'xrp': 'xrp',
    'sol': 'solana',
    'dot': 'polkadot',
    'matic': 'polygon',
    'ltc': 'litecoin',
    'doge': 'dogecoin',
    'avax': 'avalanche',
    'uni': 'uniswap',
    'trx': 'tron',
    'atom': 'cosmos',
    'algo': 'algorand',
    'xlm': 'stellar',
    'ape': 'apecoin'
}


def get_crypto(crypto=None):
    if crypto is None:
        return get_all_crypto()
    if crypto not in Crypto_list.keys(): return ('Something went wrong')
    page = requests.get(f'https://www.binance.com/en/price/{Crypto_list[crypto]}')
    if page.status_code != 200: return ('No page response')
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.findAll('meta')[2].get('content')
    price = text.split(' ')[5]
    return {crypto:price}

def get_all_crypto():
    result = {}
    for crypto in Crypto_list.keys():
        result[crypto] = (get_crypto(crypto)[crypto])
    return result

def main():
    while True:
        with open('Prices', 'w') as f:
            f.write(str(get_all_crypto()))
        time.sleep(60)

if __name__ == '__main__':
    main()
