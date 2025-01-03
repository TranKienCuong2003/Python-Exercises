import pandas as pd

def read_csv(filename):
    df = pd.read_csv(filename)
    return df

filename = "data.csv"
data = read_csv(filename)
print("Du lieu tu tep CSV la:")
print(data)
