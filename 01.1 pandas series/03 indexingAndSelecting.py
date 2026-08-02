import pandas as pd

df = pd.DataFrame(
    [
        ['Ubaid', 11, 23, 'BSCS'],
        ['Ahmad', 12, 25, 'BSSE'],
        ['Ali', 13, 19, 'BSIT'],
        ['Gull', 14, 22, 'BSCS']
    ],
    columns=['name', 'rollNO', 'age', 'degree']
)

print(df)
print(df['name']) #prints the name column
print(df[['name', 'age']]) #prints the name and age column          
print(df.loc[0]) #prints the first row of the dataframe
print(df.loc[0:2]) #prints the first 3 rows of the dataframe
print(df.loc[0:2, ['name', 'age']]) #prints the name and age column of the first 3 rows of the dataframe
print(df.iloc[0]) #prints the first row of the dataframe using index position   
print(df.iloc[0:2]) #prints the first 3 rows of the dataframe using index position
print(df.iloc[0:2, [0, 2]]) #prints the name and age column of the first 3 rows of the dataframe using index position

df.to_csv('data.csv', index=False) #exports the dataframe to csv format without index
