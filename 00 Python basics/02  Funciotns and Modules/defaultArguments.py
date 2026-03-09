#default arguments means it is not neccessary to pass that argument while calling the function
def add(a,b,c=5):
    print(f"sum is: {a+b+c}")

#calling the funciton with just two perimeters
add(5,6)  
# this will take the 3rd perimeter as 5 and prints "sum is: 16"

#lets now pass all the three perimeters
add(3,4,8) #now this will take the 3rd argument as 8 and
#the default value of c=5 is ignored in this case