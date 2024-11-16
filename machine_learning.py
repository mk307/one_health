import pandas as pd  
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

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

# Ensure X and y have consistent indices after dropping rows with NaN in target
merged_indices = X.index.intersection(y.index)
X = X.loc[merged_indices]
y = y.loc[merged_indices]

# Standardizing the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions and evaluating
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

