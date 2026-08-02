#in pnadas we mostly read excel data in csv format 
# suppose we have data 
data={
    'Names': ['Ubaid','Ahmad','Ali','Gull'],
    'Ages':[23,25,19,22],
    'City':['Buner','Peshawar','Islamabad','Qandahar']
}

# now creating a datafram from the data above
import pandas as pd
df=pd.DataFrame(data)
#if the data is stored in csv format we can import it as 
#df=pd.read_csv(data.csv)

#we can perform many operations on a data frame like
print(df.shape) #(4,3) means 4 rows and 3 columns
print(df.dtypes) #prints datatypes of each column
print(df.info()) #prints details of dataframe
print(df.head()) #prints first 5 rows of dataframe
print(df.head(3)) #prints first 3 rows of dataframe
print(df.describe()) #prints statistical analysis like mean,standard deviation,min and max value etc
print(df.isnull())  #prints true for a column which is null values and true otherwise
print(df.isna().sum()) #prints sum of null values in each column
