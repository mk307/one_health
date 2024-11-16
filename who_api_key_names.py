import requests

# WHO API endpoint for a specific indicator
url = "https://ghoapi.azureedge.net/api/MALARIA_CONF_CASES"  # Mention specific indicator code after api/

# Fetching the data
response = requests.get(url)

# Checking for successful response
if response.status_code == 200:
    data = response.json()
    
    # The top-level keys in the JSON
    print("Top-level keys:", data.keys())
    
    # Assuming 'value' is where the actual data is stored, print the keys of the first entry
    if 'value' in data and len(data['value']) > 0:
        print("Column names (keys) within 'value':", data['value'][0].keys())
    else:
        print("No data found under 'value'")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
