#pandas is used for complex data frames so we do not neeed to type such data into our code
#we can import files of csv format and excel format into our code and perform operations on it
#we can also export our data frames into csv and excel format
import pandas as pd
#reading csv file
df = pd.read_csv(r'd:\python\Advance-Python\09.1 pandas series\students_data.csv')
print(df) 
print(df.columns[0:3]) # prints the 4th column name
print(df.rows[5])