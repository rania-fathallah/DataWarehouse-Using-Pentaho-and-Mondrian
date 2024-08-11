# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine

# Define the database connection parameters
db_params = {
    'host': 'localhost',
    'database': 'database_name',
    'user': 'username',
    'password': 'password'
}

# Create the SQLAlchemy engine
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')


csv_files = {
    'input_data_2': './data_2.csv'
}


for table_name, file_path in csv_files.items():
    try:
        df = pd.read_csv(file_path)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Successfully imported '{table_name}' into PostgreSQL")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        print(f"Empty file: {file_path}")
    except Exception as e:
        print(f"Error importing '{table_name}': {e}")
