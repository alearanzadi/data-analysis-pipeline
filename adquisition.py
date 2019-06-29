import pandas as pd

def load_data(fertility_rate):
    data = pd.read_csv(fertility_rate)
    return data