import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# read csv file
df = pd.read_csv('/Users/Deen/Documents/Work/Snowflake_demo/stage/Detail_BillingProfile_ZV2C-VA2O-BG7-PGB_202305_en.csv')

# convert pandas dataframe to pyarrow table
table = pa.Table.from_pandas(df)

# write pyarrow table to parquet file
pq.write_table(table, '/Users/Deen/Documents/Work/Snowflake_demo/stage/Detail_BillingProfile_ZV2C-VA2O-BG7-PGB_202305_en.parquet')
