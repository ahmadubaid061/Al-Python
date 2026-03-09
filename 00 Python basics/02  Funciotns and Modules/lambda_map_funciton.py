#write a lambda funciton which adds two numbers 

sum=lambda x,y:x+y
print(sum(3,4))

#use map() funciton to square all the elements of a list
square=lambda x:x*x
list1=[1,2,3,4,5,6]
print(list(map(square,list1)))