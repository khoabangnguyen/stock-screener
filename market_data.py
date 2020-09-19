import alpaca_trade_api as trade_api
from config import *
import pandas as pd
import datetime
import time
from dateutil.relativedelta import relativedelta
from get_s_p_500 import symbols as sp500_symbols, sectors

api = trade_api.REST(api_key_id, secret_key, base_url='https://paper-api.alpaca.markets/')


def get_bars(symbols, time_frame='day', day_count=0, week_count=0, month_count=0, year_count=0):
    while True:
        current_raw = datetime.datetime.now()
        start_raw = (current_raw - relativedelta(days=day_count, weeks=week_count, months=month_count, years=year_count))
        start_round = pd.to_datetime(start_raw).round('1s')
        start = start_round.isoformat() + '-04:00'
        barset = api.get_barset(','.join(symbols), time_frame, after=start)

        return barset


def get_current_prices(symbols, barset):
    closing_prices = []
    for symbol in symbols:
        x = barset[symbol]
        if len(x) == 0:
            closing_prices.append('None')
        else:
            closing_prices.append(x[-1].c)
    return closing_prices

def get_volumes(symbols, barset):
    volumes = []
    for symbol in symbols:
        x = barset[symbol]
        if len(x) == 0:
            volumes.append('None')
        else:
            volumes.append(x[-1].v)
    return volumes

def get_times(symbols, barset):
    times = []
    for symbol in symbols:
        x = barset[symbol]
        if len(x) == 0:
            times.append('None')
        else:
            times.append(x[-1].t)
    return times

def get_change(symbols, barset):
    percentage_changes = []
    for symbol in symbols:
        x = barset[symbol]
        if len(x) == 0:
            percentage_changes.append('None')
        else:
            end = x[-1].c
            start = x[0].o
            percentage_changes.append("{:.2%}".format((end - start)/start))
    return percentage_changes


def create_df(symbols):
    bars = {}
    symbols_subs = [symbols[x:x + 100] for x in range(0, len(symbols), 100)]
    for sub in symbols_subs:
        barset = get_bars(sub, day_count=7)
        for i in barset:
            bars[i] = barset[i]
    closing_prices = get_current_prices(symbols, bars)
    percent_changes = get_change(symbols, bars)
    volumes = get_volumes(symbols, bars)
    times = get_times(symbols, bars)
    data = {'Name': symbols, 'Sector': sectors, 'Time': times, 'Price': closing_prices, '% Change': percent_changes, 'Volumes': volumes}
    df = pd.DataFrame(data)
    df.to_csv(r'export_dataframe.csv', index=False, header=True)
    return df


#create_df(sp500_symbols)

