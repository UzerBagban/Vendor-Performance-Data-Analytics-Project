# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import os  # For interacting with the operating system
from sqlalchemy import create_engine  # For database connection
import logging  # For logging operations
import time  # For measuring execution time

# Configure logging settings
logging.basicConfig(
    filename="logs/ingestion_db.log",  # Log file path
    level=logging.DEBUG,  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log message format
    filemode="a"  # Append mode (adds to existing log file)
)

# Create a SQLite database engine (creates 'inventory.db' if it doesn't exist)
engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''
    This function ingests a DataFrame into a database table.
    
    Parameters:
    - df (DataFrame): The pandas DataFrame to be ingested
    - table_name (str): Name of the table to create/overwrite in the database
    - engine: SQLAlchemy engine object for database connection
    '''
    # Write DataFrame to SQL database
    # 'replace' means drop the table if it exists and create a new one
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_raw_data():
    '''
    This function loads all CSV files from the 'dataset' directory,
    converts them to DataFrames, and ingests them into the database.
    '''
    start = time.time()  # Record start time for performance measurement
    
    # Loop through all files in the 'dataset' directory
    for file in os.listdir('dataset'):
        # Process only CSV files
        if '.csv' in file:
            # Read CSV file into DataFrame
            df = pd.read_csv('dataset/'+file)
            
            # Log the ingestion process
            logging.info(f'Ingesting {file} in db')
            
            # Ingest DataFrame into database (remove '.csv' extension for table name)
            ingest_db(df, file[:-4], engine)
    
    end = time.time()  # Record end time
    total_time = (end - start)/60  # Calculate total time in minutes
    
    # Log completion and total time taken
    logging.info('----------Ingestion Complete----------')
    logging.info(f'\nTotal Time Taken: {total_time} minutes')

# Main execution block
if __name__ == '__main__':
    load_raw_data()  # Execute the data loading function when script is run directly