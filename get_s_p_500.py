import pandas as pd

payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
first_table = payload[0]
symbols = first_table['Symbol'].values.tolist()
sectors = first_table['GICS Sector'].values.tolist()


