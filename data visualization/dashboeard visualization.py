import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Cybex\smart retail inteligence sysytem\note books\bussiness report dataset.csv", encoding = "latin1")

# convert date column
data["Transaction Date"] = pd.to_datetime(data["Transaction Date"])

# Revenue trend over time
monthly_revenue = (
    data.groupby(["Year", "Month"])["Revenue"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(10,5))
plt.plot(monthly_revenue.index, monthly_revenue["Revenue"])
plt.title("Revenue Trend Over Time")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.show()


# Product performance comparison
product_revenue = (
    data.groupby("product detail")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
product_revenue.plot(kind="bar")
plt.title("Product Performance Comparison")
plt.xlabel("Product Detail")
plt.ylabel("Revenue")
plt.show()


# City wise business performance
city_revenue = (
    data.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
city_revenue.plot(kind="bar")
plt.title("City Wise Business Performance")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()


# Customer behavior distribution
customer_spending = (
    data.groupby("Customer ID")["Revenue"]
    .sum()
)

plt.figure(figsize=(8,5))
plt.hist(customer_spending, bins=20)
plt.title("Customer Spending Distribution")
plt.xlabel("Customer Spending")
plt.ylabel("Number of Customers")
plt.show()


# Product market share
market_share = (
    data.groupby("product detail")["Revenue"]
    .sum()
)

plt.figure(figsize=(8,8))
plt.pie(
    market_share,
    labels=market_share.index,
    autopct="%1.1f%%"
)
plt.title("Product Market Share")
plt.show()


# Correlation heatmap
correlation_matrix = data[
    ["Quantity",
     "Price variation",
     "Discount",
     "Revenue",
     "Profit"]
].corr()

plt.figure(figsize=(8,6))
plt.imshow(correlation_matrix)
plt.colorbar()

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=90
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.title("Correlation Heatmap")
plt.show()

data.to_csv("visualized dataset.csv", index= False)