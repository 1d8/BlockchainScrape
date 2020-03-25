from bs4 import BeautifulSoup
from requests import get
import argparse
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

parser = argparse.ArgumentParser(description='Scrapes blockchain for info about BTC wallet')
parser.add_argument('-a', '--address', metavar='address', help='wallet address', required=True)
args = parser.parse_args()
address = args.address


def getBTCdetails():
    url = 'https://www.blockchain.com/btc/address/' + address
    response = get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    #finds the amount of BTC in wallet
    idleAmount = html.find_all('span', class_='sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk')
    idleAmount = idleAmount[2]
    print('Idle Amount in Wallet:', idleAmount.text)
    
    #finds the amount of transactions
    transactionAmount = html.find_all('span', class_='sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk')
    transactionAmount = transactionAmount[1]
    print('Amount of Transactions:', transactionAmount.text)
    
    #finds the amount of BTC received
    totalRec = html.find_all('span', class_='sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk')
    totalRec = totalRec[2]
    print('Total Received:', totalRec.text)
    print('\n')
    print('-' * 75)
    print('Nonexhaustive list of addresses target wallet interacted w/')
    #gathers transactions
    fromAddr = html.find_all('div', class_='sc-19pxzmk-0 iWKmuA')
    for i in fromAddr:
        i = i.text
        print(i)
    print('-' * 75)

getBTCdetails()
