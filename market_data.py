import alpaca_trade_api as trade_api
from config import *
import pandas as pd
import datetime
import time
from dateutil.relativedelta import relativedelta

api = trade_api.REST(api_key_id, secret_key, base_url='https://paper-api.alpaca.markets/')


def get_bars(symbols, day_count=0, week_count=0, month_count=0, year_count=0):
    while True:
        current_raw = datetime.datetime.now()
        start_raw = (current_raw - relativedelta(days=day_count, weeks=week_count, months=month_count, years=year_count))
        start_round = pd.to_datetime(start_raw).round('1s')
        start = start_round.isoformat() + '-04:00'
        barset = api.get_barset(','.join(symbols), 'day', after=start)

        closing_prices = []
        for symbol in symbols:
            closing_prices.append(barset[symbol][-1].c)
            #print(barset[symbol][0].__dict__['_raw'])
        data = {'name': symbols, 'price': closing_prices}
        df_marks = pd.DataFrame(data)
        print(df_marks)

        time.sleep(100000)


my_symbols = ['AAPL', 'AMZN']
get_bars(symbols=my_symbols, day_count=10)
