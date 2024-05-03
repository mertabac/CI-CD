import requests

import datetime

# Current date and time
now = datetime.datetime.now()

# Date and time 30 days ago from now
thirty_days_ago = now - datetime.timedelta(days=30)

# Converting dates to UNIX timestamps
current_timestamp = int(now.timestamp())
thirty_days_ago_timestamp = int(thirty_days_ago.timestamp())

thirty_days_ago_timestamp, current_timestamp


api_key = "cf645235-8d05-48c8-a201-ad6079668737"

def get_exchanges(api_key):
    url = "https://api.coinalyze.net/v1/exchanges"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_future_markets(api_key):
    url = "https://api.coinalyze.net/v1/future-markets"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_spot_markets(api_key):
    url = "https://api.coinalyze.net/v1/spot-markets"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_open_interest(api_key, symbols):
    url = f"https://api.coinalyze.net/v1/open-interest?symbols={symbols}"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_funding_rate(api_key, symbols):
    url = f"https://api.coinalyze.net/v1/funding-rate?symbols={symbols}"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_predicted_funding_rate(api_key, symbols):
    url = f"https://api.coinalyze.net/v1/predicted-funding-rate?symbols={symbols}"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_funding_rate_history(api_key, symbols, interval, from_timestamp, to_timestamp):
    url = f"https://api.coinalyze.net/v1/funding-rate-history?symbols={symbols}&interval={interval}&from={from_timestamp}&to={to_timestamp}"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_long_short_ratio_history(api_key, symbols, interval, from_timestamp, to_timestamp):
    url = f"https://api.coinalyze.net/v1/long-short-ratio-history?symbols={symbols}&interval={interval}&from={from_timestamp}&to={to_timestamp}"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_predicted_funding_rate_history(api_key, symbols, interval, from_timestamp, to_timestamp):
    url = f"https://api.coinalyze.net/v1/predicted-funding-rate-history?symbols={symbols}&interval={interval}&from={from_timestamp}&to={to_timestamp}"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_liquidation_history(api_key, symbols, interval, from_timestamp, to_timestamp):
    url = f"https://api.coinalyze.net/v1/liquidation-history?symbols={symbols}&interval={interval}&from={from_timestamp}&to={to_timestamp}"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_ohlcv_history(api_key, symbols, interval, from_timestamp, to_timestamp):
    url = f"https://api.coinalyze.net/v1/ohlcv-history?symbols={symbols}&interval={interval}&from={from_timestamp}&to={to_timestamp}"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

long_short_ratio_data = get_long_short_ratio_history(api_key, 'BTCUSDT', '1d')
print("Long/Short Ratio Data:", long_short_ratio_data)

