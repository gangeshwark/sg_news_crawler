import pandas as pd

data = pd.read_csv('data/all_data_new.csv', index_col='index')
print(data)
data.drop_duplicates(['source_url'], inplace=True)
data.reset_index(inplace=True)
data.drop(['index'], inplace=True, axis=1)
print(data)
# data['source_url'] = 'https://www.straitstimes.com' + data['source_url'].astype(str)

data.to_csv('data/all_data_new.csv', index_label='index')
data.to_excel('data/all_data_new.xlsx', index_label='index')
