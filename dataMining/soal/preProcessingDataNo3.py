import  pandas as pd

# membaca csv
data_startup = pd.read_csv('50_Startups.csv')

# menghitung nilai Tax
data_startup['Tax'] = (data_startup['Profit'] + data_startup['Marketing Spend'] + data_startup['Administration']) * 0.05

# output hasil
print(data_startup[['Profit', 'Marketing Spend', 'Administration', 'Tax']].head())