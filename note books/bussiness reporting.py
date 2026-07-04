import pandas as pd

data = pd.read_csv(r"D:\Cybex\smart retail inteligence sysytem\note books\behaviour analysied dataset.csv",encoding = "latin1")

# total company performance
total_revenue = data["Revenue"].sum()
total_profit = data["Profit"].sum()
total_transactions = len(data)

print("Overall Company Performance")
print("Total Revenue =", total_revenue)
print("Total Profit =", total_profit)
print("Total Transactions =", total_transactions)


# top performing products
top_products = (
    data.groupby("product detail")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Performing Products")
print(top_products)


# top performing cities
top_cities = (
    data.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Performing Cities")
print(top_cities)


# worst performing products
worst_products = (
    data.groupby("product detail")["Revenue"]
    .sum()
    .sort_values()
)

print("\nWorst Performing Products")
print(worst_products.head())


# revenue by city
city_revenue = (
    data.groupby("City")["Revenue"]
    .sum()
)

print("\nRevenue by City")
print(city_revenue)


# revenue by product detail
product_revenue = (
    data.groupby("product detail")["Revenue"]
    .sum()
)

print("\nRevenue by Product detail")
print(product_revenue)


# customer behavior insights
customer_behavior = (
    data.groupby("Customer ID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Customers")
print(customer_behavior.head(10))


# average customer spending
average_spending = data.groupby("Customer ID")["Revenue"].mean()

print("\nAverage Customer Spending")
print(average_spending.mean())


# city wise profit
city_profit = (
    data.groupby("City")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit by City")
print(city_profit)


# product wise profit
product_profit = (
    data.groupby("product detail")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit by product detail")
print(product_profit)


# save report files
top_products.to_csv("top_products_report.csv")
top_cities.to_csv("top_cities_report.csv")
city_revenue.to_csv("city_revenue_report.csv")
product_revenue.to_csv("product_revenue_report.csv")

print("\nBusiness Report Generated Successfully")


data.to_csv("bussiness report dataset.csv", index= False)

print(data.columns)