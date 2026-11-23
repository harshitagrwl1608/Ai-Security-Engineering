
import pandas as pd
import numpy as np

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Neha', 'Raj'],
    'Age': [20, 21, np.nan, 22, 23],
    'Marks': [80, np.nan, 90, 85, np.nan],
    'Salary': [20000, 25000, 30000, np.nan, 35000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()
print("Missing values in each column:")
print(df.isnull().sum())

df_filled = df.copy()

for col in ['Age', 'Marks', 'Salary']:
    df_filled[col] = df_filled[col].fillna(df_filled[col].mean())

print("\nDataFrame after filling missing values:")
print(df_filled)

df_dropped = df.dropna()

print("\nDataFrame after removing missing rows:")
print(df_dropped)
