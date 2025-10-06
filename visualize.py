import matplotlib.pyplot as plt

def plot_stock(data):
    data['MA5'] = data['Close'].rolling(5).mean()
    data['MA20'] = data['Close'].rolling(20).mean()
    #If the moving average in 5 days is trending upward and is above the moving avergae in 20 days, it generally indicates a short-term bullish trend.

    plt.figure(figsize=(10,5))
    plt.title('Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.plot(data['Date'], data['Close'], label='Close Price', linewidth=1)
    plt.plot(data['Date'], data['MA5'], label='MA5')
    plt.plot(data['Date'], data['MA20'], label='MA20')

    plt.legend()
    plt.show()