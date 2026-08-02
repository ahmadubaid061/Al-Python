'''NumPy and Pandas are the two most fundamental libraries for data science in Python. While Pandas is built on top of NumPy and relies on it for many operations, they serve different primary purposes. '''
# 1NumPy handles uniform numerical arrays. It is built for high-speed mathematical operations and matrix calculations where all data is the same type.

#2 pandas handles labeled, tabular data. It is built for data manipulation and cleaning, allowing you to work with mixed data types like a spreadsheet or SQL table.

#using numpy
#first i need to run 'pip install numpy' in terminal
import numpy as np
import time

arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape) #prints (2,3) means two rows and 3 columns
print(arr.ndim)  #prints 2 as 2D array
print(arr.dtype) #prints int64 as data type of the array

#now i want to run two different codes one with numpy and one without numpy and check the time difference

#--1 with numpy
np_array=np.array(range(1000000))
start_time=time.time() #returns current time
np_result=np_array + 5 #loops through the arraya and adds 5 with each element
end_time=time.time() #returns the current time

total_time=end_time-start_time
print("Time taken with numpy: ",total_time)

#--2 without numpy
start_time=time.time()
for i in np_array:
    i+=5

end_time=time.time()
total_time=end_time-start_time
print("Time taken without numpy: ",total_time)

#you can see clear difference between time taken by the operation 
#with numpy the operation time is reduce alot
