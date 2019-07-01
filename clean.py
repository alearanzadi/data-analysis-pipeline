import pandas as pd
from adquisition import *

def drop_cols(data):
    data.drop(["Indicator Code", "Indicator Name", "Country Code"], axis=1, inplace=True)
    return data

def drop_null(data):
    data.dropna(how='any', axis=0, inplace=True)
    return data

def clean_data(data):
    data = drop_cols(data)
    data = drop_null(data)

    df = data.set_index ("Country Name")
    df_mean = df.transpose()
    mean = df_mean.mean()
    dfmean = pd.DataFrame(mean)
    data_mean = dfmean.rename(columns={0: "Mean"})
    data_last = data_mean.sort_values("Mean", ascending=False).reset_index()
    return data_last

if __name__ == '__main__': 
    data = pd.read_csv('./fertility_rate.csv')
    data = clean_data(data)