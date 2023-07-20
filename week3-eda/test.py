import pandas as pd


data = pd.read_csv('iris_data.csv')

'''
1. Get dataframe attributes
'''

#number of rows
print(data.shape[0])

#indexes
print(data.columns.to_list())

#data types
print(data.dtypes)

'''
2. replace all "Iris-" instances from species column
'''

#1st method
data['species'] = data['species'].str.replace('Iris-', '')
print(data['species'])

#2nd method
data['species'] = data['species'].apply(lambda x: x.replace('Iris-', ''))
print(data['species'])

'''
3. Count sample numbers of each species, find mean, median, quantiles and ranges for each petal and sepal measurements
'''

values = data.species.value_counts()
print(values)

out_rows = ["mean", "median", "range", "75%", "25%"]
stats_df = data.describe()
stats_df.loc['range'] = stats_df.loc['max'] - stats_df.loc['min']
stats_df.rename({"50%": "median"}, inplace=True)
stats_df = stats_df.loc[out_rows]

print(stats_df)