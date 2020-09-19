from market_data import get_bars
from get_s_p_500 import symbols as s500
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def get_historical_prices(symbols):
    bars = {}
    symbols_subs = [symbols[x:x + 100] for x in range(0, len(symbols), 100)]
    for sub in symbols_subs:
        barset = get_bars(sub, month_count=6)
        for i in barset:
            bars[i] = barset[i]
    return bars

def plot_stock(symbol, barset):
    times = []
    prices = []
    bars = barset[symbol]
    for bar in bars:
        times.append(bar.t)
        prices.append(bar.c)
    return plt.plot(times, prices)

barset = get_historical_prices(s500)
plot_stock('AAPL', barset)