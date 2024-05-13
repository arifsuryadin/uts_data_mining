import pandas as pd
from sklearn.preprocessing import StandardScaler

# Membaca data dari CSV
data_startup = pd.read_csv('50_Startups.csv')

scaler = StandardScaler()

# scale columns
columns_to_scale = ['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']

data_startup[columns_to_scale] = scaler.fit_transform(data_startup[columns_to_scale])

# output
print(data_startup[columns_to_scale].head())
