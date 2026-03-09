#funcitons are used to reduce the complexity and improve code reusability 
#suppose i want to print the average of an array
array=[2,3,4,5,6,7,8,9]
 # i will addall the values and then divide the sum by array length
sum=0
for value in array:
    sum+=value
    
average=sum/len(array)
print(average)  

#this is okay but suppose i have 10 arrays and i want to find average of each array then i will use the same code 10 times which will be waste of time and code compexity ( alot of dupicate code
#)

# to avoid that i will jsut define a funciton and then i will call that for each array

def findAverage(arrayX):
    sum=0
    for value in arrayX:
        sum+=value
    average=sum/len(arrayX)
    print("Average is: ",average)
    
    
# now suppose i have ,ultiple arrays
array1=[1,2,3,4,5,6,7,8]
array2=[9.2,4,7,10,24,67]
array3=[37,85,24,79,14]

# i will just call that funciton for each arrray
findAverage(array1)
findAverage(array2)
findAverage(array3)