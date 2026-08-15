# E-Commerce Order Data — Exploratory Data Analysis (EDA)

## Project Title
E-Commerce Order Analysis — DecodeLabs Data Analytics Internship (Project 2)

## Description
This project analyzes an e-commerce order dataset (1,200 orders, 14 columns) to
uncover patterns, trends, and outliers before any dashboarding or modeling is done.

The script:
- Loads the order data from Excel
- Checks the dataset size and column names
- Checks for missing values
- Calculates basic statistics (mean, min, max, etc.) for Quantity, UnitPrice,
  ItemsInCart, and TotalPrice
- Breaks down orders by Product, Payment Method, Order Status, and Referral Source
- Finds the top 10 highest-value orders
- Calculates total revenue and average order value
- Detects outliers (unusually high/low orders) using the IQR method

## Dataset
`Dataset_for_Data_Analytics.xlsx` — 1,200 rows, columns include:
OrderID, Date, CustomerID, Product, Quantity, UnitPrice, ShippingAddress,
PaymentMethod, OrderStatus, TrackingNumber, ItemsInCart, CouponCode,
ReferralSource, TotalPrice.

## How to Run
1. Install the required library:
   ```
   pip install pandas openpyxl
   ```
2. Update the file path in `eda_analysis.py` to point to where your copy of
   `Dataset_for_Data_Analytics.xlsx` is saved.
3. Run the script:
   ```
   python eda_analysis.py
   ```
4. The results (missing values, statistics, top orders, revenue, outliers)
   will print directly in the terminal.

## Key Findings (fill in after running)
- Total Revenue: —
- Average Order Value: —
- Number of Outliers: —
- Top Product / Payment Method / Referral Source: —
