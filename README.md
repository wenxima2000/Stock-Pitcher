**Project introduction:**

Stocker Pitcher can automatically analyze stock data and present the most intuitive stock-related statistics that even novice investors need to pay attention to.

**Main functions:**

1.  Retrieve stock data from Yahoo Finance.
2.  Calculate the stock's average daily return, volatility, maximum gain, and maximum loss.
3.  Plot the stock's closing price and moving averages.
4.  Provide investment recommendations** based on the calculation results.


**Python Libraries Used:**

1. yfinance: To retrieve stock data from Yahoo Finance.
2. pandas: For data processing and storage, returns a DataFrame object.
3. numpy: For calculating statistics like averages and standard deviations.
4. matplotlib: For plotting stock price trends and moving averages for investers to reference and ananlyse by themselves.


**Demo:**
📈 This is Stock Pitcher, a tool to help you analyze capital market.

=== Main Menu ===
    1. Load your local stock date
    2. Fetch data online from Yahoo Finance
    3. Exit Stock Pitcher
    Please select function (1-3): 1
    Type in file path(format: data/AAPL.csv): data/LULU.csv
    Average Daily Return: -0.20%
    Volatility(Risk Level): 2.85%
    Max Daily Return: 15.89%
    Max Daily Loss: -19.80%

    === Analyze Menu ===
    1. Trend Visualization
    2. Investment advice
    3. Pitch another stock
    4. Back to main menu
    Please select function (1-4): 2

    Average return: -0.20%
    Volatility(Risk Level): 2.85%
    💬 Advice：📉 Hold for a while because returns are negative.

    === Analyze Menu ===
    1. Trend Visualization
    2. Investment advice
    3. Pitch another stock
    4. Back to main menu
    Please select function (1-4): 4

    === Main Menu ===
    1. Load your local stock date
    2. Fetch data online from Yahoo Finance
    3. Exit Stock Pitcher
    Please select function (1-3): 3
    👋 Thanks for choosing Stock Pitcher, See you!
