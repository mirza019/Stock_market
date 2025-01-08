
from Stock_fetcher import fetch_all_stock_data
from Report_generator import generate_pdf_report, save_raw_data_to_csv
from visualization import *

def main():
    print("Fetching stock market data...\n")
    stock_data = fetch_all_stock_data()

    # Generate the PDF report
    generate_pdf_report(stock_data)

    # Save the raw data to the CSV file
    save_raw_data_to_csv(stock_data)
    
if __name__ == "__main__":
    main()