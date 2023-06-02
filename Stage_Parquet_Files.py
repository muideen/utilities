import snowflake.connector
import os
from datetime import datetime

# Snowflake connection parameters
account = 'sd88081.canada-central.azure'
user = 'Muideen'
password = 'Pr0f3ss0r'
database = 'TRAINING_DB'
schema = 'RAW'
warehouse = 'compute_wh'
role = 'Data_Loader'

# Folder containing Parquet files to upload
folder_path = '/Users/Deen/Documents/Work/Utilities/Parquet_Files/'

# Name of internal stage to upload files to
stage_name = 'parquet_only_stage'

# Generate timestamp in format YYYY-MM-DD-HH-MM-SS
timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# Create stage path with timestamp
stage_path = f'@{stage_name}/{timestamp}'

# Initialize Snowflake connection
conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    database=database,
    schema=schema,
    warehouse=warehouse,
    role=role
)

# Create a Snowflake cursor to execute commands
cursor = conn.cursor()

# Create the internal stage if it does not already exist
cursor.execute(f"CREATE STAGE IF NOT EXISTS {stage_name}")

# Loop through all Parquet files in the folder and upload them to the internal stage
for filename in os.listdir(folder_path):
    if filename.endswith('.parquet'):
        filepath = os.path.join(folder_path, filename)
        cursor.execute(f"PUT 'file://{filepath}' {stage_path}/{filename}")

# Close the Snowflake connection and cursor
cursor.close()
conn.close()
