import  pandas as pd

# membaca csv
data_startup = pd.read_csv('50_Startups.csv')

# Melakukan one-hot encoding pada kolom "State"
encoded_data_startup = pd.get_dummies(data_startup, columns=['State'])

# output
print(encoded_data_startup)