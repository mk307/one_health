import requests
import pandas as pd  

# Selected World Bank indicators and their descriptions
wb_indicators = {
    'SL.TLF.ACTI.ZS': 'Labor_force',
    'SN.ITK.SVFI.ZS': 'Food_insecurity',
    'AG.LND.AGRI.ZS': 'Agricultural_land',
    'NV.AGR.TOTL.KD.ZG': 'Annual_growth'
}
wb_url = 'http://api.worldbank.org/v2/country/all/indicator/'

'''
Indicators Full Names

wb_indicators = {
    'SL.TLF.ACTI.ZS': 'Labor force participation rate, total (% of total population ages 15+)',
    'SN.ITK.SVFI.ZS': 'Prevalence of severe food insecurity in the population (%)',
    'AG.LND.AGRI.ZS': 'Agricultural land (% of land area)',
    'NV.AGR.TOTL.KD.ZG': 'Agriculture, forestry, and fishing, value added (annual % growth)'
}
'''

# Initializing an empty dataframe for merging World Bank data
wb_merged_data = pd.DataFrame()

# Looping through each indicator to retrieve data
for code, description in wb_indicators.items():
    # Requesting data for each indicator
    response = requests.get(f'{wb_url}{code}?format=json&per_page=1000&date=2000:2021')
    data = response.json()
    
    # Extracting relevant data from JSON
    records = []
    for page in data:
        if isinstance(page, list):
            for entry in page:
                if 'date' in entry and 'value' in entry:
                    records.append({
                        'Country': entry['country']['value'],
                        'Year': entry['date'],
                        code: entry['value']
                    })
    
    # Converting to dataframe and merging the data
    indicator_df = pd.DataFrame(records)
    if wb_merged_data.empty:
        wb_merged_data = indicator_df
    else:
        wb_merged_data = pd.merge(wb_merged_data, indicator_df, on=['Country', 'Year'], how='outer')

# Renaming columns with descriptions for clarity
wb_merged_data.rename(columns=wb_indicators, inplace=True)

# The final merged dataframe
print("\nMerged Data:")
print(wb_merged_data.head())

# Summary statistics and missing values
print("\nSummary Statistics:")
print(wb_merged_data.describe())

print("\nMissing Values per Column:")
print(wb_merged_data.isna().sum())

# Creating CSV
wb_merged_data.to_csv('WorldBank_merged_data.csv', index=False)
print("World Bank merged data saved as 'WorldBank_merged_data.csv'")

