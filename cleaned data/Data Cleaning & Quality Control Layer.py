import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

Data_cleaning = pd.read_csv(r"D:\Cybex\smart retail inteligence sysytem\Data\Organized_retail_dataset.csv",encoding = "latin1")

# print(Data_cleaning.head())

# Missing values in critical columns

print(Data_cleaning.isnull().sum())

# so there is no NaN value in our data set we don't need to apply fillna function

# Duplicate transactions
# 
print("Dublicate values : ", Data_cleaning.duplicated().sum())

# there is also no duplicate data

# Incorrect pricing entries

price_Quantity_check = Data_cleaning[(Data_cleaning["Price variation"] >= 0) & 
(Data_cleaning["Quantity"] >= 0)]
# print(price_Quantity_check)

# here we round he values after decimal
Data_cleaning["Revenue"] = Data_cleaning["Revenue"].round(2)
Data_cleaning["Profit"] = Data_cleaning["Profit"].round(2)

# standardize text values

Data_cleaning["product detail"] = Data_cleaning["product detail"].str.title()
Data_cleaning["City"] = Data_cleaning["City"].str.title()


# Extreme outliers affecting business metrics
Q1 = Data_cleaning["Revenue"].quantile(0.25)
Q3 = Data_cleaning["Revenue"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

data = Data_cleaning[(Data_cleaning["Revenue"] >= lower_bound) &
            (Data_cleaning["Revenue"] <= upper_bound)]


print(Data_cleaning.head())

Data_cleaning.to_csv("Cleaned data.csv", index= False)