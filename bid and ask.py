import ccxt
from pprint import pprint
import api_config as ac
exchange = ccxt.kucoinfutures({
    'adjustForTimeDifference': True,
    'apiKey': ac.API_KEY,
    'secret': ac.SECRET_KEY,
    'password': ac.PASSWORD,
})


symbol = 'LUNA/USDT:USDT'  # this format is for kucoin futures . for spot 'LUNA/USDT'


order_book = exchange.fetch_order_book(symbol)
bid = order_book['bids'][0][0]
ask = order_book['asks'][0][0]
pprint(f'first bid for {symbol} is {bid}')
pprint(f'first ask for {symbol} is {ask}')
