import csv
from datetime import datetime

def load_data(file_path):
    """ Load data from CSV file. """
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return data

def evaluate_recommendations(data):
    """ Evaluate the effectiveness of stock recommendations. """
    correct, incorrect = 0, 0
    details = []

    for item in data:
        name = item['Name']
        recommendation = item['Recommendation']
        previous_close = float(item['Previous Close'])
        current_price = float(item['Current Price'])
        price_change_percent = float(item['Price Change (%)'])

        if recommendation.startswith('Consider Buying') and price_change_percent > 1:
            correct += 1
            result = "Correct"
        elif recommendation.startswith('Consider Selling') and price_change_percent < -1:
            correct += 1
            result = "Correct"
        elif 'Hold' in recommendation and abs(price_change_percent) < 1:
            correct += 1
            result = "Correct"
        else:
            incorrect += 1
            result = "Incorrect"

        details.append(f"{name}: {result} ({recommendation} recommended, price changed by {price_change_percent}%)")

    return correct, incorrect, details

def generate_report(correct, incorrect, details, report_path):
    """ Generate a report summarizing the model's performance. """
    with open(report_path, 'w') as file:
        file.write("Stock Recommendation Performance Report\n")
        file.write("======================================\n")
        file.write(f"Total Recommendations: {correct + incorrect}\n")
        file.write(f"Correct Recommendations: {correct}\n")
        file.write(f"Incorrect Recommendations: {incorrect}\n")
        file.write("\nDetails:\n")
        for detail in details:
            file.write(detail + "\n")

def main():
    data_path = 'raw_data/Stock_Raw_Data.csv'
    report_path = 'reports/Stock_Performance_Report.txt'
    
    data = load_data(data_path)
    correct, incorrect, details = evaluate_recommendations(data)
    generate_report(correct, incorrect, details, report_path)

    print(f"Report generated at {report_path}")

if __name__ == "__main__":
    main()
