import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Replace 'path/to/your/crime_data.csv' with the actual path to your CSV file
crime_data = pd.read_csv('crime_data.csv')

# Display the first few rows of the dataset to understand its structure
print(crime_data.head())
print(crime_data.info())
print(crime_data.describe())
print(crime_data.isnull().sum())
print(crime_data.dtypes)
