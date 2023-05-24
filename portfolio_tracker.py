from pymongo import MongoClient
import yfinance as yf
import pandas as pd

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['portfolio_management_db']

# User inputs portfolio
portfolio = {
    'AAPL': 10,
    'GOOGL': 5,
    'AMZN': 2
}

# Fetch data and store in MongoDB
for stock, qty in portfolio.items():
    data = yf.download(stock, start='2020-01-01', end='2023-01-01')
    db['stocks'].insert_one({'symbol': stock, 'qty': qty, 'data': data.to_dict()})
