#there multiple ways of creating different types of arrays using numpy
import numpy as np

#--1 simple array
simpleArray=np.array([1,2,3]) # 1D array with elements 1,2,3
print(simpleArray)

#--2 2D array
twoDarray=np.array([[1,2,3],[4,5,6]])
print(twoDarray)
print(twoDarray.shape) #(2,3) 2 rows and 3 columns
print(twoDarray.ndim)  #2 means 2 dimensions

#--3 2D array with all elements zeros
zeroArray=np.zeros((2,3)) #2 rows and 3 columns
print(zeroArray)   #prints 2D array with all elments zeros

#--4 full array with a specific number
fullArray=np.full((2,3),8) #means create an array with 2 rows and 3 columns and fill the entire array with 8
print(fullArray)

#--5 arange function
arangedArr=np.arange(0,10,2) #means create an array start from 0 and upto 10 with each step skip 1 element like add each second element in the series
#it is like a loop in which iteration is incremented at each step
print(arangedArr) #0,2,4,6,8

#--6 linspace function
linspaceArr=np.linspace(0,10,4)
#means create an array which start from 0 and goes upto 10 
#the 4 perimeter means to divide the series into fours equl parts 
print(linspaceArr) #[ 0.          3.33333333  6.66666667 10.        ]


#--7 creatin identity metrix with eye() function
identityMatrix=np.eye(3) #create identity matrix with  3 rows and coloumns
print(identityMatrix)

#--8 creating array with specific datatype
datatypeArr=np.array([1,2,3],dtype=float) #converts all the numbers to float and saves it
print(datatypeArr)

#--9 converting datatype of elements of an array
newArr=datatypeArr.astype(int) #converts the data type from float to integer
print(newArr)
