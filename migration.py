import pandas as pd
from sqlalchemy import create_engine

# Step 1: Set up SQLAlchemy MySQL connection
db_user = 'root'  # Your MySQL username
db_pass = ''      # Your MySQL password
db_host = 'localhost'  # Your MySQL host (e.g., localhost or 127.0.0.1)
db_name = 'dbihrms'  # The database you want to connect to

# Creating the connection string using SQLAlchemy
connection_string = f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}"
engine = create_engine(connection_string)

# Step 2: Check if connection was successful
try:
    with engine.connect() as connection:
        print("Connected to MySQL database")

        # Step 3: Read the CSV file
        file_path = r'D:\tblempaccount.csv'  # Raw string with the "r" prefix
        df = pd.read_csv(file_path)

        # Drop rows where all elements are NaN
        df = df.dropna(how='all')

        # Step 4: Insert data into the database using to_sql
        df.to_sql('users', con=engine, if_exists='append', index=False)

        print("Data successfully imported into the database.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the engine connection
    engine.dispose()


#working on single table only