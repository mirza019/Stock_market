import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Ticker to Company Name Mapping
ticker_to_name = {
    "TSLA": "Tesla, Inc.",
    "NVDA": "NVIDIA Corporation",
    "META": "Meta Platforms, Inc.",
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc.",
    "AMZN": "Amazon.com, Inc.",
    "BRK-B": "Berkshire Hathaway Inc.",
    "JNJ": "Johnson & Johnson",
    "V": "Visa Inc.",
    "WMT": "Walmart Inc.",
    "JPM": "JP Morgan Chase & Co.",
    "PG": "Procter & Gamble Company",
    "UNH": "UnitedHealth Group Incorporated",
    "HD": "Home Depot, Inc.",
    "MA": "Mastercard Incorporated",
    "BAC": "Bank of America Corporation",
    "PFE": "Pfizer, Inc.",
    "KO": "Coca-Cola Company",
    "DIS": "Walt Disney Company",
    "CSCO": "Cisco Systems, Inc.",
    "NFLX": "Netflix, Inc.",
    "INTC": "Intel Corporation",
    "XOM": "Exxon Mobil Corporation",
    "PEP": "Pepsico, Inc.",
    "ADBE": "Adobe Inc.",
    "CRM": "Salesforce, Inc.",
    "ORCL": "Oracle Corporation",
    "CVX": "Chevron Corporation",
    "ABBV": "AbbVie Inc.",
    "T": "AT&T Inc.",
    "NKE": "Nike, Inc.",
    "COST": "Costco Wholesale Corporation",
    "MRK": "Merck & Co., Inc.",
    "CMCSA": "Comcast Corporation",
    "AMD": "Advanced Micro Devices, Inc.",
    "ABT": "Abbott Laboratories",
    "LLY": "Eli Lilly and Company",
    "UPS": "United Parcel Service, Inc.",
    "BMY": "Bristol-Myers Squibb Company",
    "DHR": "Danaher Corporation"
}

# Load raw data from the CSV file
def load_raw_data(file_path="raw_data/Stock_Raw_Data.csv"):
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])  # Ensure Date is in datetime format
        
        # Convert numeric columns to appropriate types
        numeric_columns = ['Current Price', 'Previous Close', 'Price Change (%)', 'Market Cap', 'Daily Volume']
        for col in numeric_columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')  # Convert to numeric, replacing errors with NaN

        # Drop rows with invalid numeric data
        data = data.dropna(subset=numeric_columns)

        print("Data successfully loaded and cleaned from:", file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

# Add full company names based on tickers
def add_full_names(data):
    data['Name'] = data['Ticker'].map(ticker_to_name)
    return data

# Plot candlestick chart
def plot_candlestick(data, company_name, days):
    end_date = data['Date'].max()
    start_date = end_date - timedelta(days=days)
    company_data = data[(data['Name'] == company_name) & (data['Date'] >= start_date)]

    fig = go.Figure(data=[go.Candlestick(
        x=company_data['Date'],
        open=company_data['Previous Close'],
        high=company_data['Current Price'],
        low=company_data['Current Price'] * 0.98,  # Simulating low prices
        close=company_data['Current Price']
    )])
    fig.update_layout(
        title=f"Candlestick Chart for {company_name} ({days} Days)",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white"
    )
    fig.show()

# Plot line chart for a specific company
def plot_line_chart(data, company_name, days):
    end_date = data['Date'].max()
    start_date = end_date - timedelta(days=days)
    company_data = data[(data['Name'] == company_name) & (data['Date'] >= start_date)]

    fig = go.Figure(data=[
        go.Scatter(
            x=company_data['Date'],
            y=company_data['Current Price'],
            mode='lines+markers',
            name='Current Price',
            line=dict(color='blue', width=2)
        )
    ])
    fig.update_layout(
        title=f"Line Chart for {company_name} ({days} Days)",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white"
    )
    fig.show()

# Plot volume chart for a company
def plot_volume_chart(data, company_name, days):
    end_date = data['Date'].max()
    start_date = end_date - timedelta(days=days)
    company_data = data[(data['Name'] == company_name) & (data['Date'] >= start_date)]

    fig = go.Figure(data=[
        go.Bar(
            x=company_data['Date'],
            y=company_data['Daily Volume'],
            name='Volume',
            marker_color='rgba(55, 128, 191, 0.7)'
        )
    ])
    fig.update_layout(
        title=f"Trading Volume for {company_name} ({days} Days)",
        xaxis_title="Date",
        yaxis_title="Volume",
        template="plotly_white"
    )
    fig.show()

# Plot comparison chart for all companies
def plot_comparison_chart(data):
    fig = go.Figure()
    companies = data['Name'].unique()
    for company in companies:
        company_data = data[data['Name'] == company]
        fig.add_trace(go.Scatter(
            x=company_data['Date'],
            y=company_data['Current Price'],
            mode='lines',
            name=company
        ))
    fig.update_layout(
        title="Stock Price Comparison for All Companies",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white",
        showlegend=True
    )
    fig.show()

# Main function
def main():
    # Load raw data
    file_path = "raw_data/Stock_Raw_Data.csv"
    data = load_raw_data(file_path)

    # Check if data was loaded
    if data.empty:
        print("No data to process. Exiting.")
        return

    # Add full names to the dataset
    data = add_full_names(data)

    # Default comparison chart for all companies
    print("\nGenerating default comparison chart for all companies...")
    plot_comparison_chart(data)

    print("\nAvailable Companies:")
    companies = data['Name'].unique()
    for idx, company in enumerate(companies, start=1):
        print(f"{idx}. {company}")

    company_choice = int(input("\nEnter the number corresponding to the company you want to view: "))
    selected_company = companies[company_choice - 1]

    print("\nSelect a time period:")
    print("1. Last 7 days")
    print("2. Last 30 days")
    print("3. Last 6 months")
    print("4. Last 1 year")

    time_choice = int(input("Enter your choice: "))
    time_periods = {1: 7, 2: 30, 3: 180, 4: 365}
    days = time_periods.get(time_choice, 7)

    print(f"\nGenerating charts for {selected_company} ({days} Days)...")
    plot_candlestick(data, selected_company, days)
    plot_line_chart(data, selected_company, days)
    plot_volume_chart(data, selected_company, days)

if __name__ == "__main__":
    main()
