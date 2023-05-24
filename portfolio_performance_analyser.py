# Fetch portfolio data from MongoDB
portfolio_data = db['stocks'].find()

# Calculate portfolio performance metrics and store in MongoDB
for stock in portfolio_data:
    data = pd.DataFrame(stock['data']).sort_index()
    return_ = data['Close'].pct_change().mean() * 252  # annualized return
    volatility = data['Close'].pct_change().std() * np.sqrt(252)  # annualized volatility
    db['stocks'].update_one({'_id': stock['_id']}, {'$set': {'return': return_, 'volatility': volatility}})
