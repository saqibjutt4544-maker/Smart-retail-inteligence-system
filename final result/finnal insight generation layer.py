import pandas as pd

data = pd.read_csv(r"D:\Cybex\smart retail inteligence sysytem\data visualization\visualized dataset.csv", encoding = "latin1")
print(data.columns)
# product to promote next month
product_sales = (
    data.groupby("product detail")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

best_product = product_sales.idxmax()

print("Product Recommended for Promotion Next Month:")
print(best_product)


# city needing marketing improvement
city_sales = (
    data.groupby("City")["Revenue"]
    .sum()
    .sort_values()
)

weak_city = city_sales.idxmin()

print("\nCity Needing Marketing Improvement:")
print(weak_city)


# most valuable customer group
customer_group = (
    data.groupby("Customer Segment")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

best_customer_group = customer_group.idxmax()

print("\nMost Valuable Customer Group:")
print(best_customer_group)


# finding profit leakage
profit_margin = (
    data.groupby("product detail")[["Revenue", "Profit"]]
    .sum()
)

profit_margin["Profit Margin"] = (
    profit_margin["Profit"] /
    profit_margin["Revenue"]
) * 100

profit_leakage = profit_margin.sort_values(
    by="Profit Margin"
)

print("\nProducts Showing Profit Leakage:")
print(profit_leakage.head())


# future growth trends
monthly_growth = (
    data.groupby(["Year", "Month"])["Revenue"]
    .sum()
    .pct_change() * 100
)

print("\nMonthly Growth Trends:")
print(monthly_growth.tail())


# fastest growing product
growth_product = (
    data.groupby("product detail")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

future_growth_product = growth_product.idxmax()

print("\nProduct Showing Future Growth Potential:")
print(future_growth_product)


# best city for expansion
city_profit = (
    data.groupby("City")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

expansion_city = city_profit.idxmax()

print("\nBest City for Expansion:")
print(expansion_city)


# executive summary
print("\nExecutive Business Insights")
print("Promote:", best_product)
print("Improve Marketing In:", weak_city)
print("Focus On Customer Group:", best_customer_group)
print("Expansion Opportunity:", expansion_city)
print("Growth Product:", future_growth_product)