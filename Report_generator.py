from fpdf import FPDF
import os
import csv
from datetime import datetime

def generate_pdf_report(data):
    """
    Generate a PDF report for the stock data.
    """
    # Create the reports folder if it doesn't exist
    reports_folder = "reports"
    os.makedirs(reports_folder, exist_ok=True)
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title Section
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "STOCK MARKET REPORT", ln=True, align="C")
    pdf.cell(200, 10, "Prepared by: Mirza Shaheen Iqubal", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
    pdf.ln(10)

    # Add stock data
    for entry in data:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"{entry['Ticker']} - {entry['Name']}", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f"Current Price: ${entry['Current Price']}", ln=True)
        pdf.cell(0, 8, f"Previous Close: ${entry['Previous Close']}", ln=True)
        pdf.cell(0, 8, f"Price Change (%): {entry['Price Change (%)']}%", ln=True)
        pdf.cell(0, 8, f"Status: {entry['Status']}", ln=True)
        pdf.cell(0, 8, f"Market Cap: {entry['Market Cap']}", ln=True)
        pdf.cell(0, 8, f"Daily Volume: {entry['Daily Volume']}", ln=True)
        pdf.cell(0, 8, f"Recommendation: {entry['Recommendation']}", ln=True)
        pdf.ln(5)

    # Add caption
    pdf.set_font("Arial", "I", 10)
    pdf.ln(10)
    pdf.multi_cell(0, 8, "This project work is done by Mirza Shaheen Iqubal. "
                         "This is a personal project and not financial advice. "
                         "Do not make investment decisions based on this report.", align="C")

    # Generate file name with current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = os.path.join(reports_folder, f"Stock_Report_{timestamp}.pdf")

    # Save PDF
    pdf.output(file_name)
    print(f"PDF report generated: {file_name}")

def save_raw_data_to_csv(data):
    """
    Save raw stock data to a CSV file for future analysis.
    Append new data for a new date, replace data for the same date.
    """
    # Create the raw_data folder if it doesn't exist
    raw_data_folder = "raw_data"
    os.makedirs(raw_data_folder, exist_ok=True)

    # Define the CSV file path
    csv_file = os.path.join(raw_data_folder, "Stock_Raw_Data.csv")

    # Read existing data to avoid duplicates for the same date
    existing_data = []
    if os.path.exists(csv_file):
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            existing_data = [row for row in reader]

    # Filter out rows for the current date
    date_today = datetime.now().strftime('%Y-%m-%d')
    updated_data = [row for row in existing_data if row['Date'] != date_today]

    # Add new data for the current date
    updated_data.extend(data)

    # Write back the updated data
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(updated_data)

    print(f"Raw data saved/updated in: {csv_file}")