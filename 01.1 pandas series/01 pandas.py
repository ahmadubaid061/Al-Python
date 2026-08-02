import pandas as pd
#pandas are used for data series called dataframes just like data in excel sheet where each column is a list with a label 
#just like we columns in data studentId,marks,gpa,etc 
#data frames contains several lists with labels 

simpleSeries=pd.Series([1,2,3,4,5],['a','b','c','d','e'])
print(simpleSeries.values) #prints values of the series
print(simpleSeries.index) #prints labels (headers) along with data type
print(simpleSeries.value_counts) #prints count of a each value in the series


