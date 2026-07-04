import pandas as pd
import numpy as np
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
import numpy as np


data_feature = pd.read_csv(r"D:\Cybex\smart retail inteligence sysytem\cleaned data\Cleaned data.csv",encoding= "latin1")
# print(data_feature.head())

data_feature["Customer Segment"] = np.random.choice(
    ["Regular", "Premium", "VIP"],
    len(data_feature)
)
data_feature["Transaction Date"] = pd.to_datetime(
    data_feature["Transaction Date"]
)
#monthly and yearly sales trend

data_feature["Year"] = data_feature["Transaction Date"].dt.year
data_feature["Month"] = data_feature["Transaction Date"].dt.month_name()

# Weekday vs Weekend Performance
data_feature["Day_Name"] = data_feature["Transaction Date"].dt.day_name()

data_feature["Day_Type"] = np.where(
    data_feature["Day_Name"].isin(["Saturday", "Sunday"]),
    "Weekend",
    "Weekday"
)

# Seasonal Buying Behavior

season_map = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

data_feature["Season"] = data_feature["Transaction Date"].dt.month.map(season_map)

# Profit Margin Indicators

data_feature["Profit Margin (%)"] = (
    data_feature["Profit"] / data_feature["Revenue"]
) * 100

# Customer Purchasing Frequency

customer_frequency = (
    data_feature.groupby("Customer ID")["Transaction ID"]
    .count()
)

data_feature["Purchase Frequency"] = data_feature["Customer ID"].map(customer_frequency)


product_popularity = (
    data_feature.groupby("product detail")["Quantity"]
    .sum()
    .rank(ascending=False, method="dense")
)

data_feature["Product Rank"] = data_feature["product detail"].map(product_popularity)

print(data_feature.head())
print(data_feature.columns)


data_feature.to_csv('feature_engineered_retail_dataset.csv', index = False)