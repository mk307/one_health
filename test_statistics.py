import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, pearsonr

# Merging WHO and Word Bank datasets
who_data = pd.read_csv('path.csv')
worldbank_data = pd.read_csv('path.csv')

merged_data = pd.merge(who_data, worldbank_data, on=['Year'])

# HANDLING MISSING DATA

# Replace missing values with the median (less sensitive to outliers) for numerical features
X = merged_data[['Underweight_adults', 'Malaria_cases', 'NCD_deaths']].copy()
X.fillna(X.median(), inplace=True)

# Droping rows with missing target values since they cannot contribute to the analysis
y = merged_data['Labor_force'].copy()
y = y.dropna()

# Ensuring X and y have consistent indices after handling missing data
merged_indices = X.index.intersection(y.index)
X = X.loc[merged_indices]
y = y.loc[merged_indices]

# Merging cleaned data
cleaned_data = pd.concat([X, y], axis=1)

# TEST STATISTICS

# Correlation analysis: Prevalence of underweight among adults vs. Labor force participation rate
corr_coef, p_value_corr = pearsonr(cleaned_data['Underweight_adults'], cleaned_data['Labor_force'])
print(f"Correlation Coefficient: {corr_coef}")
print(f"P-Value: {p_value_corr}")

# T-Test: Labor force participation rate vs. Prevalence of underweight among adults
# Defining groups based on median Labor_force
median_labor = cleaned_data['Labor_force'].median()
high_labor_group = cleaned_data[cleaned_data['Labor_force'] > median_labor]['Underweight_adults']
low_labor_group = cleaned_data[cleaned_data['Labor_force'] <= median_labor]['Underweight_adults']

t_stat, p_value_ttest = ttest_ind(high_labor_group, low_labor_group, equal_var=False)
print(f"T-Statistic: {t_stat}")
print(f"P-Value (T-Test): {p_value_ttest}")
