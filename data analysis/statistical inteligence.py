import pandas as pd

data = pd.read_csv(r"D:\Cybex\smart retail inteligence sysytem\data analysis\analysed dataset.csv", encoding="latin1")

# ---------------------------------------------------
# Average and Median Sales Behavior
# ---------------------------------------------------

average_sales = data["Revenue"].mean()
median_sales = data["Revenue"].median()

print("\nAverage Sales:")
print(average_sales)

print("\nMedian Sales:")
print(median_sales)


# ---------------------------------------------------
# Variability in Customer Spending
# Standard Deviation measures how much customer
# spending varies from the average spending.
# ---------------------------------------------------

customer_spending_variability = data["Revenue"].std()

print("\nCustomer Spending Variability:")
print(customer_spending_variability)


# ---------------------------------------------------
# Distribution of Product Prices
# Provides statistical summary of product prices.
# ---------------------------------------------------

price_distribution = data["Price variation"].describe()

print("\nProduct Price Distribution:")
print(price_distribution)


# ---------------------------------------------------
# Correlation Between Discount and Revenue
# Values close to:
#  1  -> strong positive relation
#  0  -> no relation
# -1  -> strong negative relation
# ---------------------------------------------------

discount_sales_correlation = data["Discount"].corr(data["Revenue"])

print("\nDiscount and Revenue Correlation:")
print(discount_sales_correlation)


# ---------------------------------------------------
# Risk Analysis of Low Performing Products
# Products with revenue below average are considered
# low-performing products.
# ---------------------------------------------------

average_product_revenue = (
    data.groupby("product detail")["Revenue"]
    .sum()
    .mean()
)

low_performing_products = (
    data.groupby("product detail")["Revenue"]
    .sum()
)

low_performing_products = (
    low_performing_products[
        low_performing_products < average_product_revenue
    ]
)

print("\nLow Performing Products:")
print(low_performing_products)


# ---------------------------------------------------
# Revenue Distribution Statistics
# ---------------------------------------------------

print("\nRevenue Statistics:")
print(data["Revenue"].describe())


# ---------------------------------------------------
# Profit Distribution Statistics
# ---------------------------------------------------

print("\nProfit Statistics:")
print(data["Profit"].describe())


# ---------------------------------------------------
# Customer Purchase Frequency Statistics
# ---------------------------------------------------

purchase_frequency = (
    data.groupby("Customer ID")["Transaction ID"]
    .count()
)

print("\nCustomer Purchase Frequency Statistics:")
print(purchase_frequency.describe())


# ---------------------------------------------------
# Most and Least Expensive Product Types
# ---------------------------------------------------

product_price_analysis = (
    data.groupby("product detail")["Price variation"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Product Prices:")
print(product_price_analysis)


print(data.shape)
data.to_csv("statistical dataset.csv", index=False)
