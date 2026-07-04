import numpy as np
import pandas as pd

# Load the data 
retail_data = pd.read_csv(r"D:\Cybex\smart retail inteligence sysytem\Data\retail transaction.csv",encoding = "latin1")
# print(retail_data.head())
# print(retail_data.isnull().sum())
# print("Dublicated values in data set : ",retail_data.duplicated().sum())

# Calculate the Revinue

retail_data['Revenue'] = (
    retail_data['Quantity']*
    retail_data['Price variation']*
    (1 - retail_data['Discount'])
)

# Profit is estimated from revenue

profit = np.random.uniform(0.10, 0.30, len(retail_data))
retail_data["Profit"] = retail_data["Revenue"] * profit

# Cities and stores are properly mapped

store_mapping = {
    "Islamabad": ("Store A"),
    "Lhore": "Store B",
    "Faisabad": "Store C",
    "Karachi": "Store D",
    "Peshawar": "Store E",
    "Queeta": "Store F"
}

retail_data["Store"] = retail_data["City"].map(store_mapping)

print(retail_data)


retail_data.to_csv("Organized_retail_dataset.csv",index= False)