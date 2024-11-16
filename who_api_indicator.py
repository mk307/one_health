import requests
import pandas as pd

# WHO API endpoint for indicators
indicator_url = "https://ghoapi.azureedge.net/api/Indicator"

# Fetching indicators metadata
response = requests.get(indicator_url)
if response.status_code == 200:
    indicators = response.json()['value']  # List of indicators
    indicators_df = pd.DataFrame(indicators)  

    # Filtering by a keyword to find relevant indicators
    keyword = "ncd"
    filtered_indicators = indicators_df[indicators_df['IndicatorName'].str.contains(keyword, case=False)]
    df = filtered_indicators

    # Displaying the indicator names and codes
    print(filtered_indicators[['IndicatorName', 'IndicatorCode']])
    df.to_csv("indicator_data_ncd.csv", index=False)
else:
    print(f"Failed to fetch indicators. Status code: {response.status_code}")
