import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

'''
4. Calculate mean, median petal/sepal length for each species
'''

mean = data.groupby('species').mean()
median = data.groupby('species').median()
print(mean, median)

mean_median = data.groupby('species').agg(['mean', 'median'])
print(mean_median)


'''
5. Make a scatter plot of sepal_length vs sepal_width using Matplotlib. Label the axes and give the plot a title.
'''

plt.figure()
axs = plt.axes()
axs.scatter(data.sepal_length, data.sepal_width)
axs.set(xlabel="sepal_length", ylabel="sepal_width", title="sepal_length vs sepal_width")

'''
6. Make a histogram of any one of the four features. Label axes and title it as appropriate.
'''

plt.figure()
axs = plt.axes()
axs.hist(data.sepal_length, bins=25)
axs.set(xlabel="sepal_length", ylabel="sample number", title="sepal_length histogram")

'''
7. Now create a single plot with histograms for each feature (petal_width, petal_length, sepal_width, sepal_length) overlayed. If you have time, next try to create four individual histogram plots in a single figure, where each plot contains one feature.
'''

axs = data.plot.hist(bins=25)
axs.set_xlabel('Size in cm')

fig, axs = subplots = plt.subplots(2, 2)
fig.suptitle('Size vs Frequency')
axs[0, 0].hist(data.petal_width, bins=25)
axs[0, 0].set(xlabel="petal_width(cm)", ylabel="Frequency")
axs[0, 1].hist(data.petal_length, bins=25)
axs[0, 1].set(xlabel="petal_length(cm)", ylabel="Frequency")
axs[1, 0].hist(data.sepal_width, bins=25)
axs[1, 0].set(xlabel="sepal_width(cm)", ylabel="Frequency")
axs[1, 1].hist(data.sepal_length, bins=25)
axs[1, 1].set(xlabel="sepal_length(cm)", ylabel="Frequency")



#using pandas
data.hist(bins=25)


'''
8. Using Pandas, make a boxplot of each petal and sepal measurement.
'''
data.boxplot(by='species')


'''
9. Make a pairplot with Seaborn to examine the correlation between each of the measurements.
'''

sns.pairplot(data, hue='species');

plt.show()