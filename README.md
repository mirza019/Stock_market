# Stock Recommendation Evaluation and Reporting

This project automates the evaluation of stock recommendations based on historical price changes. It fetches real-time stock data from Yahoo Finance, saves it into a CSV file, evaluates the accuracy of recommendations, generates detailed reports, and appends raw data for future analysis. The entire process is automated in a pipeline.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Data Pipeline Overview](#data-pipeline-overview)
4. [Prerequisites and Installation](#prerequisites-and-installation)
5. [How to Run](#how-to-run)
6. [Outputs](#outputs)
7. [File Descriptions](#file-descriptions)
8. [Project Structure](#project-structure)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

---

## Project Overview

This project is designed to evaluate the accuracy of stock recommendations using historical stock data. The process includes:
- **Data Fetching**: Real-time stock data is fetched from Yahoo Finance using the `yfinance` library.
- **Data Storage**: The fetched data is saved into a CSV file (`raw_data/Stock_Input_Data.csv`).
- **Analysis and Evaluation**: The recommendations are evaluated for accuracy, and detailed reports are generated.
- **Raw Data Management**: Processed data is appended to a historical CSV file for future analysis.

---

## Features

1. **Automated Data Pipeline**:
   - Fetches stock data, saves it into a CSV, and processes it automatically.

2. **Recommendation Analysis**:
   - Evaluates whether stock recommendations (Buy, Sell, Hold) were accurate based on price changes.

3. **Model Performance Evaluation**:
   - Generates a summary report of recommendation accuracy.

4. **Raw Data Management**:
   - Appends processed data into a historical file for tracking.

---

## Data Pipeline Overview

1. **Data Fetching**:
   - The `Stock_fetcher.py` script fetches real-time stock data for a predefined list of tickers from Yahoo Finance using the `yfinance` library.
   - Key metrics retrieved include:
     - **Current Price**
     - **Previous Close**
     - **Price Change (%)**
     - **Market Cap**
     - **Daily Volume**
     - **Recommendation** (generated based on stock performance).

2. **CSV Creation**:
   - The fetched data is saved into `raw_data/Stock_Input_Data.csv` in the required format for analysis.

3. **Analysis and Evaluation**:
   - The `main.py` script reads the CSV file, evaluates recommendations for accuracy, and generates:
     - **Recommendation Report**: A detailed analysis of individual recommendations.
     - **Model Accuracy Report**: A summary of overall performance.

4. **Raw Data Management**:
   - Processed data is appended to the historical file (`raw_data/raw_data.csv`) for future reference.

---

## Prerequisites and Installation

```bash
# Prerequisites
# Ensure you have Python installed (3.6 or higher)

# Installation

# 1. Clone the Repository
git clone https://github.com/mirza019/Stock_market.git
cd Stock_market

# 2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3. Install Dependencies
pip install -r requirements.txt


## How to Run

```bash
# Run the Main Script
python main.py

.
├── raw_data/
│   ├── Stock_Input_Data.csv      # Input data file
│                                 # Historical raw data file
│
├── reports/
│   ├── recommendation_report.txt # Detailed recommendation analysis
│   ├── model_accuracy_report.txt # Model accuracy summary
│
├── main.py                       # Main script to orchestrate the project
├── evaluate_performance.py       # Script to evaluate stock recommendation accuracy
├── Report_generator.py           # Script to generate reports
├── Stock_fetcher.py              # Script to fetch and process stock data
├── Utils.py                      # Utility functions
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

This project is licensed under the MIT License

main.py:
    Orchestrates the execution of the stock evaluation process.

evaluate_performance.py:
    Contains functions to evaluate the accuracy of stock recommendations.

Report_generator.py:
    Generates detailed reports for recommendation analysis and model accuracy.

Stock_fetcher.py:
    Fetches and processes stock data from external sources.

Utils.py:
    Utility functions used throughout the project.

raw_data/Stock_Input_Data.csv:
    The input CSV file with stock data.


reports/recommendation_report.pdf:
    A report analyzing the correctness of individual recommendations with current date.

reports/model_accuracy_report.txt:
    A summary of the recommendation model's accuracy.

requirements.txt:
    List of Python dependencies required for the project.

Outputs: 
    Recommendation Report:

    Location: reports/recommendation_report.txt
    Content: Detailed analysis of individual stock recommendations, including correctness and reasoning.
    Model Accuracy Report:

    Location: reports/model_accuracy_report.txt
    Content: Summary of the recommendation model's overall performance, including the total number of correct and incorrect recommendations.
    Raw Data CSV:

    Location: raw_data/raw_data.csv
    Content: Appends historical stock data for future reference and tracking.