import yfinance as yf
import mplfinance as mpf
import numpy as np


def plot_candlestick(symbol, period="1mo", interval="1h"):
    ticker = yf.Ticker(symbol)
    hist_data = ticker.history(period=period, interval=interval)
    
    mpf.plot(hist_data, type='candle', style='charles',
             title=f"{symbol} Candlestick Chart",
             ylabel='Price (USD)')

def main():
    symbol = input("Please enter the symbol (e.g., 'AAPL' for Apple, 'BTC-USD' for Bitcoin): ")
    period = input("Please enter the time period for data (e.g., '1mo' for one month, '1y' for one year): ")
    interval = input("Please enter the data interval (e.g., '1h' for hourly, '1d' for daily): ")
    
    plot_candlestick(symbol, period, interval)

if __name__ == "__main__":
    main()
