import numpy as np

def analyze_returns(data):
    """Calculates daily returns, average return, and volatility."""
    data['Daily Return'] = data['Close'].pct_change()
    avg_return = np.mean(data['Daily Return']) * 100
    volatility = np.std(data['Daily Return']) * 100
    max_return = np.max(data['Daily Return']) * 100
    min_return = np.min(data['Daily Return']) * 100

    print(f"Average Daily Return: {avg_return:.2f}%")
    print(f"Volatility(Risk Level): {volatility:.2f}%")
    print(f"Max Daily Return: {max_return:.2f}%")
    print(f"Max Daily Loss: {min_return:.2f}%")

    with open("result.txt", "w") as f:
        f.write(f"Average Daily Return: {avg_return:.2f}%\n")
        f.write(f"Volatility(Risk Level): {volatility:.2f}%\n")
        f.write(f"Max Daily Return: {max_return:.2f}%\n")
        f.write(f"Max Daily Loss: {min_return:.2f}%\n")

    return data