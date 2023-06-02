import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import datetime

# set the directory where the CSV files are located
csv_directory = '/Users/Deen/Documents/Work/Utilities/Data_Generators'

# get the current timestamp up to minutes
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')

# set the directory where the Parquet files should be saved
parquet_directory = '/Users/Deen/Documents/Work/Utilities/Parquet_Files/{}'.format(timestamp)

# create the directory for the Parquet files
os.makedirs(parquet_directory)

# iterate over all CSV files in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        # read the CSV file into a pandas dataframe
        csv_filepath = os.path.join(csv_directory, filename)
        df = pd.read_csv(csv_filepath)

        # convert the pandas dataframe to a pyarrow table
        table = pa.Table.from_pandas(df)

        # save the pyarrow table as a Parquet file
        parquet_filename = os.path.splitext(filename)[0] + '.parquet'
        parquet_filepath = os.path.join(parquet_directory, parquet_filename)
        pq.write_table(table, parquet_filepath)

        print('Saved {} as {}'.format(filename, parquet_filename))
