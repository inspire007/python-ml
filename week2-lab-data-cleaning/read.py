import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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

duplicates = housing[housing.duplicated(['PID'])]
print(duplicates)