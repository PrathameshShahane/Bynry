import pandas as pd
from sqlalchemy import create_engine

# Establish a connection to the database
engine = create_engine('postgresql://Bynryuser:password@localhost:5432/BynryData')

# Extract data from the database
df = pd.read_sql_query("SELECT * FROM consumer_data", engine)

# Map the data to the SMART360 schema
df['First Name], df['Last Name'] = df['Name'].str.split(' ', 1).str
df = df.drop(columns=['Name'])

# Load the data into the SMART360 platform
df.to_sql('smart360_consumer_data', engine, if_exists='append')
