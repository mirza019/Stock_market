import yfinance as yf
from datetime import datetime
from Utils import calculate_change, suggest_action

# List of expanded stock tickers
tickers = [
    "TSLA", "NVDA", "META", "AAPL", "MSFT", "GOOGL", "AMZN", "BRK-B", "JNJ", "V",
    "WMT", "JPM", "PG", "UNH", "HD", "MA", "BAC", "PFE", "KO", "DIS",
    "CSCO", "NFLX", "INTC", "XOM", "PEP", "ADBE", "CRM", "ORCL", "CVX", "ABBV",
    "T", "NKE", "COST", "MRK", "CMCSA", "AMD", "ABT", "LLY", "UPS", "BMY", "DHR"
]

def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.info

        name = data.get("shortName", "N/A")
        current_price = data.get("currentPrice", 0.0)
        previous_close = data.get("previousClose", 0.0)
        market_cap = data.get("marketCap", "N/A")
        daily_volume = data.get("volume", "N/A")

        price_change, status = calculate_change(current_price, previous_close)
        recommendation = suggest_action(price_change, daily_volume)

        return {
            "Ticker": ticker,
            "Name": name,
            "Current Price": current_price,
            "Previous Close": previous_close,
            "Price Change (%)": price_change,
            "Status": status,
            "Market Cap": market_cap,
            "Daily Volume": daily_volume,
            "Recommendation": recommendation,
            "Date": datetime.now().strftime('%Y-%m-%d')
        }

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return {
            "Ticker": ticker,
            "Name": "Error",
            "Current Price": "Error",
            "Previous Close": "Error",
            "Price Change (%)": "Error",
            "Status": "Error",
            "Market Cap": "Error",
            "Daily Volume": "Error",
            "Recommendation": "Error",
            "Date": datetime.now().strftime('%Y-%m-%d')
        }

def fetch_all_stock_data():
    stock_data = []
    for ticker in tickers:
        data = fetch_stock_data(ticker)
        stock_data.append(data)
    return stock_data
