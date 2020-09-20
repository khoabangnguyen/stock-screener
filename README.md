# Stock Screener
	
Stock screener built with Python and HTML, using Alpaca's Stock Trading API.

Currently includes:

	Current price (USD)
	Change ($)
	Change (%)
	Volume
	Sector

EPS (TTM), P/E, and market cap will be implemented soon.
  
Data is refreshed every 30 seconds during market hours.

## Usage

#### Create a config.py file with:

```python
api_key_id = 'YOUR-ALPACA-API-KEY-ID'
secret_key = 'YOUR-ALPACA-SECRET-KEY-ID'
driver_path = r'YOUR-FILE-PATH-TO-CHROMEDRIVER'
```
#### market_data.py

Timestamps, prices, changes (absolute and percent), and volume (EPS, P/E, and market cap coming soon)

#### get_s_p_500.py

Tickers and sectors

#### plotter.py

Historical price data over an adjustable period

#### sheets_updater.py

Updates spreadsheet using Google Sheets API

#### main

Flask server

