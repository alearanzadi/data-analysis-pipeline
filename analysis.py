import adquisition
from clean import *
from scraping import *

def merge(df, df1):
    data_merge = df.merge(df1, on='Country Name', how='inner')
    data_merge.sort_values('gdp', ascending=False)
    data_desc = data_merge.describe()
    return data_merge, data_desc
