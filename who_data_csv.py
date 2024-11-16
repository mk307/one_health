import requests
import pandas as pd

# Selected WHO indicators with their descriptions
who_indicators = {
    'NCD_BMI_18C': 'Underweight_adults',
    'MALARIA_CONF_CASES': 'Malaria_cases',
    'NCD_DTH_TOT': 'NCD_deaths'
}
who_url = 'https://ghoapi.azureedge.net/api/'

'''
Indicators Full Names

who_indicators = {
    'NCD_BMI_18C': 'Prevalence of underweight among adults, BMI < 18 (crude estimate) (%)',
    'MALARIA_CONF_CASES': 'Number of confirmed malaria cases',
    'NCD_DTH_TOT': 'Total NCD Deaths (in thousands)'
}
'''

# Initializing an empty dataframe for merging WHO data
who_merged_data = pd.DataFrame()

# Looping through each indicator to retrieve and merge data
for code, description in who_indicators.items():
    # Requesting data for each indicator
    response = requests.get(f'{who_url}{code}')
    data = response.json()
    
    # Extracting relevant data from JSON
    records = []
    for entry in data['value']:
        records.append({
            'Country': entry['SpatialDim'],
            'Year': entry['TimeDim'],
            description: entry['NumericValue']  # Using descriptive name as column name
        })
    
    # Converting to dataframe for the current indicator
    indicator_df = pd.DataFrame(records)
    
    # Merging with the existing WHO data
    if who_merged_data.empty:
        who_merged_data = indicator_df
    else:
        who_merged_data = pd.merge(who_merged_data, indicator_df, on=['Country', 'Year'], how='outer')

# The final merged DataFrame
print("\nMerged Data:")
print(who_merged_data.head())

# Summary statistics and missing values
print("\nSummary Statistics:")
print(who_merged_data.describe())

print("\nMissing Values per Column:")
print(who_merged_data.isna().sum())

# Creating CSV
who_merged_data.to_csv('WHO_merged_data.csv', index=False)
print("WHO merged data saved as 'WHO_merged_data.csv'")

