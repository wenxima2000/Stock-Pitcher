import yfinance as yf

def fetch_data(stock_pitch: str, start="2024-01-01", end=None):

    print(f"📡 We are getting {stock_pitch} data from Yahoo Finance from 2024 till now...")
    data = yf.download(stock_pitch, start=start, end=end, auto_adjust=True, progress=True)

    if data.empty:
        print("Oops, seems no data for this stock. Please try a valid one.")
        return None

    data.columns = data.columns.get_level_values(0) #we want the closing price for the stock pitch, so we keep level_value(0)

    data = data.reset_index()[['Date', 'Close']] #for clearly illustration, we only keep date and close price for the annalysis

    filename = f"data/{stock_pitch}.csv"
    data.to_csv(filename, index=False)

    print(f"✅ Stock data fetched and stored in {filename} successfully.")
    return data