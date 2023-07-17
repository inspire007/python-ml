import pandas as pd

#data = pd.read_csv('data.txt', header=None, delim_whitespace=True)
data = pd.read_csv('data.txt', header=None, sep=' ')
print(data.to_numpy())