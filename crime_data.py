import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, zscore, f_oneway, chi2_contingency

# Load and preview the dataset
print("Loading the crime dataset...")
crime_data = pd.read_csv('crime_data.csv')
print("Dataset preview:")
print(crime_data.head())
print("Data summary:")
print(crime_data.info())
print("Statistical summary:")
print(crime_data.describe())
print("Missing values:")
print(crime_data.isnull().sum())
print("Data types:")
print(crime_data.dtypes)

# Drop unnecessary columns for analysis
print("Dropping irrelevant columns...")
columns_to_drop = ['Mocodes', 'Vict Sex', 'Vict Descent', 'Premis Cd', 'Premis Desc', 'Weapon Used Cd',
                   'Weapon Desc', 'Crm Cd 1', 'Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Cross Street']
crime_data = crime_data.drop(columns=columns_to_drop, axis=1)

# Handle missing values and data types
print("Handling missing values and data types...")
crime_data['DR_NO'] = crime_data['DR_NO'].astype('object')
crime_data['Date Rptd'] = pd.to_datetime(crime_data['Date Rptd'])
crime_data['DATE OCC'] = pd.to_datetime(crime_data['DATE OCC'])
crime_data['Status'] = crime_data['Status'].astype('category')

crime_data['TIME OCC'] = crime_data['TIME OCC'].astype(str).str.zfill(4)
crime_data['TIME OCC'] = pd.to_datetime(crime_data['TIME OCC'], format='%H%M', errors='coerce')
crime_data['Vict Age'] = crime_data['Vict Age'].replace(0, np.nan)

# Remove duplicates
print("Removing duplicate entries...")
crime_data.drop_duplicates(inplace=True)

# First Visualization: Top 10 Crimes by Crime Description
print("Creating a bar plot for top 10 crime descriptions...")
plt.figure(figsize=(12, 6))
top_10_crimes = crime_data['Crm Cd Desc'].value_counts().head(10).sort_values(ascending=False)
sns.barplot(x=top_10_crimes.index, y=top_10_crimes.values, palette='Set2', hue=top_10_crimes.index, legend=False)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Crimes by Crime Description')
plt.xlabel('Crime Description')
plt.ylabel('Crime Count')
plt.tight_layout()
plt.show()

# Second Visualization: Crime Distribution by Area
print("Creating a bar plot for crime distribution by area...")
plt.figure(figsize=(12, 6))
area_crime_count = crime_data['AREA NAME'].value_counts().head(10)
sns.barplot(x=area_crime_count.index, y=area_crime_count.values, palette='viridis', hue=area_crime_count.index, legend=False)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Areas by Crime Count')
plt.xlabel('Area')
plt.ylabel('Crime Count')
plt.tight_layout()
plt.show()

# Third Visualization: Crime Distribution by Year
print("Creating a line plot for crime distribution by year...")
crime_data['Year'] = crime_data['Date Rptd'].dt.year
crime_by_year = crime_data['Year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x=crime_by_year.index, y=crime_by_year.values, marker='o', color='blue')
plt.title('Crime Distribution by Year')
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.show()

# Fourth Visualization: Victim Age Distribution
print("Creating a histogram for victim age distribution...")
crime_data['Vict Age Category'] = pd.cut(crime_data['Vict Age'],
                                          bins=[0, 18, 30, 40, 50, 60, 70, 80, 100],
                                          labels=['0-18', '19-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81+'],
                                          include_lowest=True)
plt.figure(figsize=(12, 6))
sns.histplot(data=crime_data, x='Vict Age Category', bins=30, color='purple', discrete=True)
plt.title('Victim Age Distribution (Excluding Zero Age)')
plt.xlabel('Age Categories')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Fifth Visualization: Victim Age vs. Crime Type (Boxplot)
print("Creating a boxplot for victim age distribution by crime type...")
plt.figure(figsize=(15, 6))

# Reduce the number of crime categories if needed, for better readability
top_crime_categories = crime_data['Crm Cd Desc'].value_counts().head(10).index
crime_data_filtered = crime_data[crime_data['Crm Cd Desc'].isin(top_crime_categories)]

# Updated boxplot with 'hue' and without 'palette' in deprecated way
sns.boxplot(x='Crm Cd Desc', y='Vict Age', data=crime_data_filtered, hue='Crm Cd Desc', palette='Set3', legend=False)
plt.xticks(rotation=45, ha='right')
plt.title('Victim Age Distribution by Top 10 Crime Types')
plt.xlabel('Crime Type')
plt.ylabel('Victim Age')
plt.tight_layout()
plt.show()

# Descriptive Statistics
print("Calculating descriptive statistics for victim age...")
mean_age = crime_data['Vict Age'].mean()
median_age = crime_data['Vict Age'].median()
mode_age = crime_data['Vict Age'].mode()[0]
std_dev = crime_data['Vict Age'].std()
variance = crime_data['Vict Age'].var()
age_skewness = skew(crime_data['Vict Age'].dropna())
age_kurtosis = kurtosis(crime_data['Vict Age'].dropna())

print(f"Mean: {mean_age}, Median: {median_age}, Mode: {mode_age}")
print(f"Standard Deviation: {std_dev}, Variance: {variance}")
print(f"Skewness: {age_skewness}, Kurtosis: {age_kurtosis}")

# Correlation Analysis
print("Creating a correlation heatmap...")
numeric_columns = crime_data.select_dtypes(include=[np.number])
correlation_matrix = numeric_columns.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.show()

# Hypothesis Testing (ANOVA)
print("Performing ANOVA test to see if there are differences in victim age by area...")
crime_counts_by_area = crime_data.groupby('AREA NAME')['DR_NO'].count()
crime_data_groups = [crime_data[crime_data['AREA NAME'] == area]['Vict Age'].dropna() for area in crime_data['AREA NAME'].unique()]
f_statistic, p_value = f_oneway(*crime_data_groups)
print("F-statistic:", f_statistic)
print("P-value:", p_value)
if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference in crime rates across areas.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in crime rates across areas.")

# Chi-Square Test for Categorical Data
print("Performing Chi-Square test for association between crime type and case status...")
contingency_table = pd.crosstab(crime_data['Status'], crime_data['Crm Cd Desc'])
chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-Square statistic: {chi2_stat}, P-value: {p_val}")

# Time Series Analysis
print("Creating a time series plot for monthly crime trends...")
crime_data['Month'] = crime_data['DATE OCC'].dt.month
monthly_crimes = crime_data.groupby('Month')['DR_NO'].count()

plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_crimes.index, y=monthly_crimes.values)
plt.title('Monthly Crime Trends')
plt.xlabel('Month')
plt.ylabel('Crime Count')
plt.tight_layout()
plt.show()

# Z-score Outlier Detection
print("Identifying outliers in victim age using Z-score...")
victim_age_cleaned = crime_data['Vict Age'].dropna()  # Remove NaN values from 'Vict Age'
z_scores = zscore(victim_age_cleaned)

# Find the indices of the outliers
outlier_indices = victim_age_cleaned.index[z_scores > 3]

# Get the outliers from the original data
outliers = crime_data.loc[outlier_indices, 'Vict Age']
print(f"Outliers in Victim Age:\n{outliers}")
