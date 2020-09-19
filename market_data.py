import alpaca_trade_api as trade_api
from config import *
import pandas as pd
import datetime
import time
from dateutil.relativedelta import relativedelta
from get_s_p_500 import symbols as sp500_symbols

api = trade_api.REST(api_key_id, secret_key, base_url='https://paper-api.alpaca.markets/')


def get_bars(symbols, time_frame='day', day_count=0, week_count=0, month_count=0, year_count=0):
    while True:
        current_raw = datetime.datetime.now()
        start_raw = (current_raw - relativedelta(days=day_count, weeks=week_count, months=month_count, years=year_count))
        start_round = pd.to_datetime(start_raw).round('1s')
        start = start_round.isoformat() + '-04:00'
        barset = api.get_barset(','.join(symbols), time_frame, after=start)

        return barset


def get_current_prices(symbols):
    closing_prices = []
    symbols_subs = [symbols[x:x+100] for x in range(0, len(symbols), 100)]
    count = 0
    for sub in symbols_subs:
        barset = get_bars(sub, day_count=1)
        for symbol in sub:
            x = barset[symbol]
            if len(x) == 0:
                #print(symbol)
                closing_prices.append('None')
            else:
                closing_prices.append(x[-1].c)
    return closing_prices


def create_df(symbols):
    data = {'Name': symbols, 'Price': get_current_prices(symbols)}
    df = pd.DataFrame(data)
    df.to_csv(r'export_dataframe.csv', index=False, header=True)
    return df


print(create_df(sp500_symbols))

