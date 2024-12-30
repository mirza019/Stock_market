# Stock Recommendation Evaluation and Reporting

This project automates the evaluation of stock recommendations based on historical price changes. It processes input CSV files, evaluates the accuracy of recommendations, generates detailed reports, and appends raw data for future analysis.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites and Installation](#prerequisites-and-installation)
4. [How to Run](#how-to-run)
5. [Outputs](#outputs)
6. [File Descriptions](#file-descriptions)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

---

## Project Overview

This project is designed to evaluate the accuracy of stock recommendations using historical stock data. It processes input CSV files, evaluates the success of recommendations (e.g., Buy, Sell, Hold), and generates:
- **Recommendation Report**: Evaluates individual stock recommendations.
- **Model Accuracy Report**: Summarizes the overall performance of the recommendation model.
- **Raw Data CSV**: Appends input data into a historical CSV file for future analysis.

---

## Features

1. **Recommendation Analysis**:
   - Evaluate whether stock recommendations were accurate based on price changes.
2. **Model Performance Evaluation**:
   - Generate a summary report of recommendation accuracy.
3. **Raw Data Management**:
   - Append new input data to an existing raw data file for historical tracking.

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
# Stock Recommendation Evaluation and Reporting

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
