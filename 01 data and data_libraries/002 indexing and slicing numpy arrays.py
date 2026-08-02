import numpy as np
array=np.array([[10,20,30],[40,50,60],[70,80,90]])

#indexing a 2d array requires two peramters i for rows and j for columns
print(array[2,2]) #90  means itme at row 2 ,column 2 which is 90

# slicing 
print(array[0:2,1:3])  #means row 0 to 2 and column 1 to 3 output is: [[20 30],[50 60]]

print(array[::2,::2]) #prints each second row and 2nd column  like row 0,2,4 and col 0,2,4

print(array[0,:2]) #means print row 0 upto column 2 (stop before col 2)

print(array[1:2,0]) #means print row 1 upto column 0 which is just a single element 40
