import pandas as pd

data = pd.read_csv(r"D:\Cybex\smart retail inteligence sysytem\data analysis\statistical dataset.csv",encoding = "latin1")
# converting date column into datetime
data["Transaction Date"] = pd.to_datetime(data["Transaction Date"])

# extracting date information
data["Year"] = data["Transaction Date"].dt.year
data["Month"] = data["Transaction Date"].dt.month_name()
data["Day"] = data["Transaction Date"].dt.day
data["Weekday"] = data["Transaction Date"].dt.day_name()

# if you have time in your data then extract hour also
# data["Hour"] = data["Transaction Date"].dt.hour


# Daily sales fluctuations
daily_sales = data.groupby("Day")["Revenue"].sum()

print("Daily Sales")
print(daily_sales)


# Weekly sales trends
weekly_sales = data.groupby("Weekday")["Revenue"].sum()

print("\nWeekly Sales")
print(weekly_sales)


# Monthly growth cycles
monthly_sales = data.groupby("Month")["Revenue"].sum()

print("\nMonthly Sales")
print(monthly_sales)


# Long term expansion pattern
yearly_sales = data.groupby("Year")["Revenue"].sum()

print("\nYearly Sales")
print(yearly_sales)


# Peak business hours
# this works only if Hour column exists

# peak_hours = data.groupby("Hour")["Revenue"].sum()
# print("\nPeak Business Hours")
# print(peak_hours)


# Seasonal spikes
seasonal_sales = data.groupby("Season")["Revenue"].sum()

print("\nSeasonal Sales")
print(seasonal_sales)


# Weekend and weekday performance
weekend_sales = data.groupby("Day_Type")["Revenue"].sum()

print("\nWeekend vs Weekday Sales")
print(weekend_sales)


# Slow business periods
slow_periods = monthly_sales.sort_values().head(3)

print("\nSlow Business Periods")
print(slow_periods)


# Highest sales month
best_month = monthly_sales.idxmax()

print("\nBest Sales Month")
print(best_month)


# Highest sales weekday
best_day = weekly_sales.idxmax()

print("\nBest Sales Day")
print(best_day)

data.to_csv("behaviour analysied dataset.csv", index = False)