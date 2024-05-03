import pandas as pd
import yfinance as yf
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import mplfinance as mpf
import numpy as np

def get_input(prompt, valid_responses=None):
    """Prompt the user for input until a valid response is given."""
    while True:
        response = input(prompt).strip().lower()
        if valid_responses is None or response in valid_responses:
            return response
        print("Invalid input, please try again. Valid responses are:", valid_responses)

def collect_tickers(market_type):
    """Collect ticker symbols from user input until 'q' is entered."""
    tickers = []
    prompt = 'Please give a ticker symbol (q to quit): '
    while True:
        ticker_input = get_input(prompt)
        if ticker_input == 'q':
            break
        ticker = f"{ticker_input.upper()}-USD" if market_type == 'c' else ticker_input.upper()
        tickers.append(ticker)
    return tickers

def download_data(tickers, start, end):
    """Download historical data for given tickers from Yahoo Finance."""
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
    """Add delta columns for volume and adjusted close price."""
    for symbol, data in dfs.items():
        data['Volume Delta'] = data['Volume'].diff().fillna(0)
        data['Close Delta'] = data['Adj Close'].diff().fillna(0)

def calculate_returns(dfs):
    """Calculate simple and logarithmic returns."""
    for symbol, data in dfs.items():
        data['Returns'] = data['Adj Close'].pct_change().fillna(0)
        data['Log Returns'] = np.log(data['Adj Close'] / data['Adj Close'].shift(1)).fillna(0)

def plot_returns(data, ticker):
    """Plot returns and log returns for a given ticker."""
    plt.figure(figsize=(14, 7))
    plt.subplot(2, 1, 1)
    plt.plot(data['Returns'], label='Returns', color='blue')
    plt.title(f'{ticker} Returns')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(data['Log Returns'], label='Log Returns', color='green')
    plt.title(f'{ticker} Log Returns')
    plt.legend()

    plt.tight_layout()
    plt.show()

def calculate_correlation(dfs):
    """Calculate and return correlation matrix for given features in dataframes."""
    combined_data = pd.concat([df[feature] for feature, df in dfs.items()], axis=1)
    return combined_data.corr()

def plot_heatmap(corr, title):
    """Plot a heatmap for the correlation matrix."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title(title)
    plt.show()

def plot_candlestick(data, symbol):
    """Plot candlestick chart for given data."""
    mpf.plot(data, type='candle', title=f"{symbol} Candlestick Chart", style='charles', volume=True, mav=(3,6,9))

def main():
    """Main function to run the financial data analysis."""
    market = get_input("Which Market (C for Crypto Market, S for Stock Market): ", ['c', 's'])
    period = int(get_input('Please give a number for analyzing period: '))
    end = dt.datetime.now()
    start = end - dt.timedelta(days=period)
    tickers = collect_tickers(market)
    print("Your Tickers:", tickers)
    
    if tickers:
        dfs = download_data(tickers, start, end)
        add_delta_columns(dfs)
        calculate_returns(dfs)
        
        for ticker, df in dfs.items():
            plot_returns(df, ticker)  # Plot both returns and log returns
        
        volume_correlation = calculate_correlation(dfs, 'Volume Delta')
        plot_heatmap(volume_correlation, "Volume Correlation Matrix")
        
        individual_correlations = calculate_correlation(dfs)
        # Assuming plotting individual correlations if needed

if __name__ == "__main__":
    main()

print('actions test_2')