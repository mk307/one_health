import pandas as pd
from sqlalchemy import create_engine

# Load datasets
who_data = pd.read_csv('E:\My Data\Skills Development\Programming\Python\Projects\One Health - Sustainability\Data\WHO_merged_data.csv')
worldbank_data = pd.read_csv('E:\My Data\Skills Development\Programming\Python\Projects\One Health - Sustainability\Data\WorldBank_merged_data.csv')

# Creating a connection to the MySQL database
engine = create_engine('mysql+mysqlconnector://who_wb_user:OneHealth_Sustainability@localhost/who_wb_databases')

# Insert data into SQL tables
who_data.to_sql('who_data', engine, if_exists='replace', index=False)
worldbank_data.to_sql('worldbank_data', engine, if_exists='replace', index=False)
