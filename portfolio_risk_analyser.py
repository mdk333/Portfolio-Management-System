from scipy.stats import norm

# Fetch portfolio data from MongoDB
portfolio_data = db['stocks'].find()

# Calculate Value at Risk (VaR) and Conditional Value at Risk (CVaR)
for stock in portfolio_data:
    data = pd.DataFrame(stock['data']).sort_index()
    returns = data['Close'].pct_change()
    VaR = norm.ppf(1 - 0.05, returns.mean(), returns.std())
    CVaR = returns[returns <= VaR].mean()
    db['stocks'].update_one({'_id': stock['_id']}, {'$set': {'VaR': VaR, 'CVaR': CVaR}})
