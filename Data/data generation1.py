# Layer 1 generating synthetic sales transaction records

import pandas as pd
import numpy as np



n = 1000
start_date = pd.Timestamp('2024-01-01')
end_date = pd.Timestamp('2025-12-31')

random_dates = pd.to_datetime(
    np.random.randint(
        start_date.value // 10**9,
        end_date.value // 10**9,
        n
    ),
    unit='s'
)


data = pd.DataFrame({
    'Transaction ID' : ['TTD'+ str(i) for i in range(1 ,n+1)],
    'Customer ID' : np.random.randint(10000, 99999, n),
    'product detail': np.random.choice([
        'Electronics','Grocery','clothing','sports','book'],n
        ),
    'City': np.random.choice([
        'Islamabad','Lhore','Faisabad','Karachi','Peshawar','Queeta'
    ],n),
    'Quantity' : np.random.randint(1, 20, n),
    'Price variation' : np.random.randint(50, 5000,n),
    
    'Discount' : np.random.uniform(0,0.30, n),
    'Transaction Date': random_dates
    
})

data.to_csv("retail transaction.csv", index = False)
print(data.head())

