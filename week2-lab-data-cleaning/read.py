import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

housing = pd.read_csv('Ames_Housing_Data1.tsv', sep='\t')

print(housing.head(10))
print(housing.info())
print(housing["SalePrice"].describe())

housing_num = housing.select_dtypes(include=['float64', 'int64'])
housing_num_corr = housing_num.corr()['SalePrice'][:-1]

#print(housing_num_corr)

top_features = housing_num_corr[abs(housing_num_corr) > 0.5].sort_values(ascending=False)
print(top_features)

'''
sns.pairplot(data=housing_num, x_vars=['Overall Qual'], y_vars=['SalePrice'])
sns.pairplot(data=housing_num, x_vars=['Garage Yr Blt'], y_vars=['SalePrice'])
plt.tight_layout()
plt.show()
'''
'''
print("Skewness:", housing['SalePrice'].skew())
sns.displot(housing['SalePrice'])
logged_price = np.log(housing['SalePrice'])
sns.displot(logged_price)
print("Skewness:", logged_price.skew())
plt.show()
'''

#duplicates = housing[housing.duplicated(['PID'])]
#print(duplicates)

'''
missing = housing.isnull().sum().sort_values(ascending=False).head(20)
missing.plot(kind='bar')
plt.show()
'''

#sns.boxplot(x=housing['SalePrice'])
'''
housing.plot.scatter(x='Gr Liv Area', y='SalePrice')
plt.show()
'''

'''
outliner = housing.sort_values('Gr Liv Area', ascending=False)[:2]
print(outliner)

outliner_removed = housing.drop(housing.index[[1499, 2181]])
outliner_removed.plot.scatter(x='Gr Liv Area', y='SalePrice')
plt.show()
'''

housing['Lot_Area_Z'] = stats.zscore(housing['Lot Area'])
print(housing['Lot_Area_Z'])

lot_area_outliner_indexes = housing['Lot_Area_Z'][abs(housing['Lot_Area_Z']) > 3].index.to_numpy()
print(lot_area_outliner_indexes)

lot_area_outliner_removed = housing.drop(housing.index[lot_area_outliner_indexes])
print(lot_area_outliner_removed)