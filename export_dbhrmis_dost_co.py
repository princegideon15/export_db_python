import pandas as pd
import os
from sqlalchemy import create_engine

# Step 1: Set up SQLAlchemy MySQL connection
db_user = 'root'
db_pass = ''
db_host = 'localhost'  # Your MySQL host (e.g., localhost)
db_name = 'dbhrmis'

# Creating the connection string using SQLAlchemy
connection_string = f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}"
engine = create_engine(connection_string)

# engine = sqlalchemy.create_engine('mysql://myuser:mypassword@192.168.1.100:3306/mydb')

# Step 2: Create a directory to store the CSV files
output_dir = "D:/import_to_ihrms/hrmis_exported_csv_files"
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Step 3: Get a list of all tables in the database
tables_query = "SHOW TABLES"
tables = pd.read_sql(tables_query, engine)  # Use SQLAlchemy engine here

# Step 4: Loop through each table and export to CSV
for table_name in tables.values.flatten():  # Flatten the result to get table names
    query = f"SELECT * FROM {table_name}"
    
    # Use pandas to fetch the table data and export it to CSV
    data = pd.read_sql(query, engine)
    
    # Create the CSV file path using the table name
    csv_file = os.path.join(output_dir, f"{table_name}.csv")
    
    # Export the table data to CSV (index=False means no row numbers)
    data.to_csv(csv_file, index=False)
    
    print(f"Exported {table_name} to {csv_file}")

# Step 5: Close the database connection (optional, handled by SQLAlchemy)
engine.dispose()

print("All tables have been exported successfully.")

#working