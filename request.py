import pandas as pd

excel_file = 'hongkong.csv'

df = pd.read_csv(excel_file)
mylist=[10]

ls=df.loc[df['accommodates'].isin(mylist)]

# print(ls)


# Use getitem ([]) to iterate over columns in pandas DataFrame
for index, row in ls.iterrows():
    print(row['accommodates'], row['amenities'])
 