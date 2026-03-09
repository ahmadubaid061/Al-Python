# write a funciton which prints factorial of a number
# factorial is the product of all numbers in range of 1 and number the numbre included
# like factorial of 4 = 1*2*3*4

def factorial(n):
    if(n==0 or n==1):
        return 1
    return factorial(n-1)*n

print(factorial(5))