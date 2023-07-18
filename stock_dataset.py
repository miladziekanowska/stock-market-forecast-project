# pip install yahoo_fin

# importing libraries and modules
import pandas as pd
import numpy as np
import yahoo_fin.stock_info as yh
from datetime import datetime
from dateutil.relativedelta import relativedelta
import warnings

warnings.filterwarnings("ignore", message="Parsing dates")

# Creating dictionary with stock prices of Dow Jones stocks from last 3 years
ticker_list = yh.tickers_dow()
initial_data = {}

start_date = (datetime.now() - relativedelta(years=3)).strftime('%d-%m-%Y')
end_date = datetime.today().strftime('%d-%m-%Y')

for ticker in ticker_list:
    initial_data[ticker] = yh.get_data(ticker, start_date=start_date, end_date=end_date, index_as_date = False,
                                           interval="1d")

# creating a new feature with the proprtion of the day's closing price to the previous day's closing price
for key in initial_data:
    initial_data[key]['dailychange'] = initial_data[key]['close'].div(initial_data[key]['close'].shift(1))
    initial_data[key]['dailychange'].fillna(1, inplace=True)

# creating the desired form of the data
stock_data = {}
for key in initial_data:
    stock_data[key] = initial_data[key][['date', 'close', 'dailychange']]


# creating dataframe with all data for visualization

dataset = pd.concat(initial_data.values()).reset_index(drop=True)

dataset.to_csv('data/stock_initial_data.csv')


print('Stock data ready to use!')