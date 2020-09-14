import alpaca_trade_api as trade_api
from config import *
import pandas as pd
import datetime
import time
from dateutil.relativedelta import relativedelta

api = trade_api.REST(api_key_id, secret_key, base_url='https://paper-api.alpaca.markets/')


def get_bars(symbols="", time_num=0, time_type="years"):
    while True:
        current_raw = datetime.datetime.now()
        start_raw = (current_raw - relativedelta(days=7))
        start_round = pd.to_datetime(start_raw).round('1s')
        start = start_round.isoformat() + '-04:00'
        barset = api.get_barset('AAPL', 'day', after=start)
        aapl_bars = barset['AAPL']

        print(aapl_bars)

        time.sleep(1)


get_bars()
