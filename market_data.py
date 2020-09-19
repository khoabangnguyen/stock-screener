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

def get_screener_data(symbols, barset):
    current_prices = []
    changes = []
    percent_changes = []
    volumes = []
    times = []
    for symbol in symbols:
        x = barset[symbol]
        if len(x) == 0:
            current_prices.append('None')
            changes.append('None')
            percent_changes.append('None')
            volumes.append('None')
            times.append('None')
        else:
            current = x[-1].c
            start = x[0].o
            current_prices.append(current)
            changes.append(current - start)
            percent_changes.append("{:.2%}".format((current - start) / start))
            volumes.append(x[-1].v)
            times.append(x[-1].t)
    data = {'Name': symbols, 'Time': times, 'Price': current_prices, 'Change': changes, '% Change': percent_changes, 'Volumes': volumes, 'Sector': sectors }
    return data

def create_df(symbols):
    bars = {}
    symbols_subs = [symbols[x:x + 100] for x in range(0, len(symbols), 100)]
    for sub in symbols_subs:
        barset = get_bars(sub, day_count=7)
        for i in barset:
            bars[i] = barset[i]
    df = pd.DataFrame(get_screener_data(symbols, bars))
    df.to_csv(r'export_dataframe.csv', index=False, header=True)
    return df


#create_df(sp500_symbols)

