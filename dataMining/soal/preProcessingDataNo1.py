import  pandas as pd

# membaca csv
data_startup = pd.read_csv('50_Startups.csv')

#  Mengecek apakah ada nilai kosong di seluruh dataset
print(data_startup.isnull().any())

# Menghitung nilai rata-rata dari kolom "R&D Spend"
rd_spend_mean = data_startup['R&D Spend'].mean()

# Mengisi nilai kosong dengan nilai rata-rata
data_startup.fillna({'R&D Spend': rd_spend_mean}, inplace=True)

# Mengecek lagi apakah ada nilai kosong di seluruh dataset
print(data_startup.isnull().any())
