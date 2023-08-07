import pandas as pd
import plotly.express as px

gasoline = pd.read_csv('18100001.csv')

#get data overview

print(gasoline.head())
print(gasoline.shape)
print(gasoline.columns.to_list())
print(gasoline.info())
print(gasoline.isnull().sum())

#Data wrangling
#select only the rows we need

data = gasoline[['REF_DATE', 'GEO', 'Type of fuel', 'VALUE']]
data = data.rename(columns={'REF_DATE': 'DATE', 'Type of fuel': 'TYPE'})
data[['City', 'Province']] = gasoline['GEO'].str.split(',', n=1, expand=True)

#Format datetime column
data['DATE'] = pd.to_datetime(data['DATE'], format='%b-%y')
data['Month'] = data['DATE'].dt.month_name().str.slice(stop=3)
data['Year'] = data['DATE'].dt.year

print(data.head())

#price value stats
print(data.VALUE.describe())
print(data.GEO.unique().tolist())

#filtering
print(data[data['City'] == 'Calgary'])

#multiple filtering
multi = data[(data['City'] == 'Calgary') | (data['City'] == 'Toronto')]
print(multi)

cities = ['Calgary', 'Toronto']
print(data[data.City.isin(cities)])

'''
In this exercise, please use the examples shown above, to select the data that shows the price of the 'household heating fuel', in Vancouver, in 1990.
'''

res = data[(data.TYPE == 'Household heating fuel') & (data.City == 'Vancouver') & (data.Year == 1990) ]
print(res)

'''
In this exercise, please select the data that shows the price of the 'household heating fuel', in Vancouver, in the years of 1979 and 2021.
'''

res = data[(data.TYPE == 'Household heating fuel') & (data.City == 'Vancouver') & ( (data.Year == 1979) | (data.Year == 2021)) ]
print(res)

'''
group by filtering method
'''
prices = data.groupby('GEO')['VALUE'].describe()
print(prices)

'''
use groupby() method to group by the maximum value of gasoline prices, for each month.
'''

print(data.groupby('Month')['VALUE'].max())

'''
use plotly.express or other libraries, to plot the annual average gasoline price, per year, per gasoline type.
'''
d = data.groupby(['Year', 'TYPE'])['VALUE'].mean().reset_index()

fig = px.line(d, x='Year', y='VALUE', color='TYPE')
fig.update_traces(mode="markers+lines")
fig.update_layout(title="Annual average gasoline price, per year, per gasoline type", yaxis_title="Price of gasoline", xaxis_title="Year")
fig.show()


