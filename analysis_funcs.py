import pandas as pd
import yfinance as yf
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import mplfinance as mpf

def get_input(prompt, valid_responses=None):
    while True:
        response = input(prompt).strip().lower()  # Kullanıcı girişini al ve düzenle
        if valid_responses is None or response in valid_responses:
            return response
        print("Invalid input, please try again.")

def collect_tickers(market_type):
    tickers = []
    while True:
        ticker_input = get_input('Please give a ticker symbol (q to quit): ')
        if ticker_input == 'q':
            break
        if market_type == 'c':
            ticker = f"{ticker_input.upper()}-USD"
        else:
            ticker = ticker_input.upper()
        tickers.append(ticker)
    return tickers

def download_data(tickers, start, end):
    dataframes = {}
    for ticker in tickers:
        try:
            data = yf.download(ticker, start=start, end=end)
            dataframes[ticker] = data
            print(f"Data downloaded for {ticker}")
        except Exception as e:
            print(f"Failed to download data for {ticker}: {e}")
    return dataframes

def add_delta_columns(dfs):
    for symbol, data in dfs.items():
        data['Volume Delta'] = data['Volume'].diff().fillna(0)
        data['Close Delta'] = data['Adj Close'].diff().fillna(0)

def calculate_correlation(dfs, feature):
    combined_data = pd.DataFrame()
    for symbol, df in dfs.items():
        combined_data[symbol] = df[feature]
    return combined_data.corr()

def calculate_individual_correlation(dfs):
    correlations = {}
    for symbol, df in dfs.items():
        correlations[symbol] = df.corr()
    return correlations

def plot_heatmap(corr, title):
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title(title)
    plt.show()

def plot_candlestick(data, symbol):
    mpf.plot(data, type='candle', title=f"{symbol} Candlestick Chart", style='charles', volume=True, mav=(3,6,9))


def main():
    market = get_input("Which Market (C for Crypto Market, S for Stock Market): ", ['c', 's'])
    period = int(get_input('Please give a number for analyzing period: '))
    end = dt.datetime.now()
    start = end - dt.timedelta(days=period)
    tickers = collect_tickers(market)
    print("Your Tickers:", tickers)
    
    if tickers:
        dfs = download_data(tickers, start, end)
        add_delta_columns(dfs)
        
        volume_correlation = calculate_correlation(dfs, 'Volume Delta')
        plot_heatmap(volume_correlation, "Volume Correlation Matrix")
        
        individual_correlations = calculate_individual_correlation(dfs)
        for symbol, corr in individual_correlations.items():
            plot_heatmap(corr, f"Correlation Matrix for {symbol}")
        for ticker, df in dfs.items():
            plot_candlestick(df, ticker)

if __name__ == "__main__":
    main()
