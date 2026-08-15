import pandas as pd

# STEP 1: Load the dataset from Excel into a table (called a "DataFrame")
df = pd.read_excel(r"D:\Data Analytics\Data Analytics Project 2\Dataset for Data Analytics.xlsx")

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

# How many rows (orders) and columns (fields) does the data have?
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# Show the name of every column in the dataset
print("\nColumn Names:")
print(df.columns.tolist())

# --------------------------------------------------

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)

# Check each column for empty/blank cells (missing data)
print(df.isnull().sum())

# --------------------------------------------------

print("\n" + "=" * 50)
print("DESCRIPTIVE STATISTICS")
print("=" * 50)

# Get quick stats (average, min, max, etc.) for the number columns
print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].describe())

# --------------------------------------------------

print("\n" + "=" * 50)
print("PRODUCT ANALYSIS")
print("=" * 50)

# Count how many times each product was ordered
print(df["Product"].value_counts())

# --------------------------------------------------

print("\n" + "=" * 50)
print("PAYMENT METHOD ANALYSIS")
print("=" * 50)

# Count how many orders used each payment method
print(df["PaymentMethod"].value_counts())

# --------------------------------------------------

print("\n" + "=" * 50)
print("ORDER STATUS ANALYSIS")
print("=" * 50)

# Count how many orders are Delivered, Cancelled, Pending, etc.
print(df["OrderStatus"].value_counts())

# --------------------------------------------------

print("\n" + "=" * 50)
print("REFERRAL SOURCE ANALYSIS")
print("=" * 50)

# Count where customers came from
print(df["ReferralSource"].value_counts())

# --------------------------------------------------

print("\n" + "=" * 50)
print("TOP 10 HIGHEST ORDERS")
print("=" * 50)

# Sort orders by price (highest first) and show the top 10
print(
    df[["OrderID", "Product", "TotalPrice"]]
    .sort_values(by="TotalPrice", ascending=False)
    .head(10)
)

# --------------------------------------------------

print("\n" + "=" * 50)
print("TOTAL REVENUE")
print("=" * 50)

# Add up the price of every order to get total money earned
total_revenue = df["TotalPrice"].sum()
print("Total Revenue:", total_revenue)

# --------------------------------------------------

print("\n" + "=" * 50)
print("AVERAGE ORDER VALUE")
print("=" * 50)

# Find the average amount spent per order
average_order = df["TotalPrice"].mean()
print("Average Order Value:", round(average_order, 2))

# --------------------------------------------------

print("\n" + "=" * 50)
print("OUTLIER DETECTION")
print("=" * 50)

# Outliers = orders that are unusually cheap or unusually expensive

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

# Orders below this are unusually low
lower_limit = Q1 - 1.5 * IQR

# Orders above this are unusually high
upper_limit = Q3 + 1.5 * IQR

# Keep only outlier records
outliers = df[
    (df["TotalPrice"] < lower_limit)
    | (df["TotalPrice"] > upper_limit)
]

print("Number of Outliers:", len(outliers))

print("\nTop Outliers:")
print(
    outliers[["OrderID", "Product", "TotalPrice"]]
    .sort_values(by="TotalPrice", ascending=False)
    .head()
)

# --------------------------------------------------

print("\n" + "=" * 50)
print("EXPORTING DATASET")
print("=" * 50)

# Save dataset to a new Excel file
df.to_excel(
    r"D:\Data Analytics\Data Analytics Project 2\EDA_Processed_Dataset.xlsx",
    index=False
)

print("EDA_Processed_Dataset.xlsx saved successfully!")

# --------------------------------------------------

print("\nEDA COMPLETED SUCCESSFULLY")