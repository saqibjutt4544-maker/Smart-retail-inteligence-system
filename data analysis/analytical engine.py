import pandas as pd

data = pd.read_csv(r"D:\Cybex\smart retail inteligence sysytem\data features\feature_engineered_retail_dataset.csv", encoding= "latin1")

data["Transaction Date"] = pd.to_datetime(data["Transaction Date"])

product_revenue = (
    data.groupby("product detail")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

city_profit = (
    data.groupby("City")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

customer_segment_sales = (
    data.groupby("Customer Segment")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

monthly_sales = (
    data.groupby(["Year", "Month"])["Revenue"]
    .sum()
    .reset_index()
)

yearly_sales = (
    data.groupby("Year")["Revenue"]
    .sum()
    .sort_values()
)

category_dominance = (
    data.groupby("product detail")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

revenue_growth = yearly_sales.pct_change() * 100

monthly_profit = (
    data.groupby(["Year", "Month"])["Profit"]
    .sum()
    .reset_index()
)

customer_frequency = (
    data.groupby("Customer ID")["Transaction ID"]
    .count()
    .sort_values(ascending=False)
)

store_performance = (
    data.groupby("Store")[["Revenue", "Profit"]]
    .sum()
    .sort_values(by="Revenue", ascending=False)
)

weekday_weekend_sales = (
    data.groupby("Day_Type")["Revenue"]
    .sum()
)

seasonal_sales = (
    data.groupby("Season")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_customers = (
    data.groupby("Customer ID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("Highest Revenue Products")
print(product_revenue)

print("\nMost Profitable Cities")
print(city_profit)

print("\nCustomer Segments Buying the Most")
print(customer_segment_sales)

print("\nMonthly Sales Trend")
print(monthly_sales)

print("\nYearly Sales Trend")
print(yearly_sales)

print("\nMarket Dominating Categories")
print(category_dominance)

print("\nRevenue Growth Trend (%)")
print(revenue_growth)

print("\nMonthly Profit Fluctuation")
print(monthly_profit)

print("\nCustomer Buying Patterns")
print(customer_frequency.head(10))

print("\nStore Performance Comparison")
print(store_performance)

print("\nWeekday vs Weekend Sales")
print(weekday_weekend_sales)

print("\nSeasonal Buying Behaviour")
print(seasonal_sales)

print("\nTop 10 Customers")
print(top_customers)


data.to_csv("analysed dataset.csv", index = False)