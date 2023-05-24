import matplotlib.pyplot as plt

# Fetch portfolio data from MongoDB
portfolio_data = db['stocks'].find()

# Calculate portfolio value and plot asset allocation
total_value = sum(stock['qty'] * pd.DataFrame(stock['data'])['Close'][-1] for stock in portfolio_data)
portfolio_data = db['stocks'].find()  # re-fetch data due to cursor exhaustion
labels, sizes = [], []
for stock in portfolio_data:
    value = stock['qty'] * pd.DataFrame(stock['data'])['Close'][-1]
    labels.append(stock['symbol'])
    sizes.append(value / total_value * 100)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
