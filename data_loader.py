import pandas as pd

def load_data(filename) -> pd.DataFrame: #trying to build a structured dataframe with pandas, instead of manually decompose huge data
    data = pd.read_csv(filename)
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date') #want to calculate the daily return and draw graphs in time order
    return data