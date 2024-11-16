import pandas as pd
from sqlalchemy import create_engine

# Load datasets
who_data = pd.read_csv('path.csv')
worldbank_data = pd.read_csv('path.csv')

# Creating a connection to the MySQL database
engine = create_engine('mysql+mysqlconnector://[user_name]:[password]@localhost/[database_name]')

# Insert data into SQL tables
who_data.to_sql('who_data', engine, if_exists='replace', index=False)
worldbank_data.to_sql('worldbank_data', engine, if_exists='replace', index=False)
