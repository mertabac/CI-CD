<<<<<<< Updated upstream
print("Hello")
=======
import yfinance as yf
import mplfinance as mpf

def plot_candlestick(symbol, period="1mo", interval="1h"):

    ticker = yf.Ticker(symbol)
    hist_data = ticker.history(period=period, interval=interval)

    mpf.plot(hist_data, type='candle', style='charles',
             title=f"{symbol} Candlestick Chart",
             ylabel='Price (USD)',
             show_nontrading=True)

def main():

    symbols_input = input("Please enter the symbols separated by commas (e.g., 'AAPL, MSFT, BTC-USD'): ")
    symbols = [symbol.strip() for symbol in symbols_input.split(',')]
    period = input("Please enter the time period for data (e.g., '1mo' for one month, '1y' for one year): ")
    interval = input("Please enter the data interval (e.g., '1h' for hourly, '1d' for daily): ")

    for symbol in symbols:
        plot_candlestick(symbol, period, interval)

if __name__ == "__main__":
    main()

>>>>>>> Stashed changes
