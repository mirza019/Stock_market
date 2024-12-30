import csv

def calculate_change(current_price, previous_close):
    if previous_close == 0:
        return "N/A", "No Change"
    price_change = ((current_price - previous_close) / previous_close) * 100
    status = "Increase" if price_change > 0 else "Decrease" if price_change < 0 else "No Change"
    return round(price_change, 2), status

def suggest_action(price_change, volume):
    """
    Suggest whether to invest, hold, or sell based on price change and volume.
    """
    if price_change == "N/A":
        return "No Data"
    if price_change > 2:  # High positive price change
        return "Consider Selling (high demand)"
    elif price_change < -2:  # Significant drop
        return "Consider Buying (potential rebound)"
    elif volume > 10_000_000:  # High trading volume
        return "Hold (high activity)"
    else:
        return "No Action Needed"
    

def load_csv_data(file_path):
    """Utility to load data from CSV."""
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
    except FileNotFoundError:
        print("CSV file not found:", file_path)
    return data

def evaluate_performance(differences, current_data):
    """Evaluate the model's performance based on the differences."""
    correct_predictions = 0
    for diff in differences:
        ticker = diff['Ticker']
        current_data = next((item for item in current_data if item['Ticker'] == ticker), None)
        if not current_data:
            continue
        # Assume `next_day_price` is the price of the stock on the next day (to be fetched separately)
        if diff['Previous Recommendation'] == 'Buy' and float(current_data['next_day_price']) > float(current_data['Current Price']):
            correct_predictions += 1
        elif diff['Previous Recommendation'] == 'Sell' and float(current_data['next_day_price']) < float(current_data['Current Price']):
            correct_predictions += 1
        elif diff['Previous Recommendation'] == 'Hold' and float(current_data['next_day_price']) == float(current_data['Current Price']):
            correct_predictions += 1

    accuracy = (correct_predictions / len(differences)) * 100 if differences else 100
    if accuracy > 75:
        return "Excellent"
    elif accuracy > 50:
        return "Good"
    elif accuracy > 25:
        return "Average"
    else:
        return "Poor"

def print_comparison(differences):
    """Prints differences between old and new recommendations."""
    for diff in differences:
        print(f"Ticker: {diff['Ticker']}")
        print(f"  Previous Recommendation: {diff['Previous Recommendation']} on {diff['Previous Date']}")
        print(f"  Current Recommendation: {diff['Current Recommendation']} on {diff['Current Date']}\n")
