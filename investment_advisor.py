def give_investment_advice(data):
    avg_return = data['Daily Return'].mean() * 100
    volatility = data['Daily Return'].std() * 100

    if avg_return > 0.5 and volatility < 2:
        advice = "📈 Can be considered for medium-term holding with low volatility and stable returns."
    elif avg_return > 0.2 and volatility > 2:
        advice = "⚡ High-volatility and high-potential stocks are suitable for short-term trading or observing entry opportunities."
    elif avg_return < 0:
        advice = "📉 Hold for a while because returns are negative. But you can also try short selling."
    else:
        advice = "💤 Do diversify investments because of the normal performance."

    print(f"\nAverage return: {avg_return:.2f}%")
    print(f"Volatility(Risk Level): {volatility:.2f}%")
    print(f"💬 Advice：{advice}")