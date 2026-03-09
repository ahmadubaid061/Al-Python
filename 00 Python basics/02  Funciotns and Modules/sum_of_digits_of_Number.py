#write a function which returns the sum of all the digits of a number
def sum_of_digits(n):
    if n==0:
        return 0
    return n%10 + sum_of_digits(n//10)

# the last line of the funcitons means
# n%10 means the last digit at tenth position. n%10 of 112 is 2
# n//10 means the last digit excluded. n//10 of 112 is 11
# first i am gonna try n%10 and n//10 then i will call the funciton

num=112
print(num%10) #returns 2
print(num//10) #returns 11

# now call the funciton for 112
print(sum_of_digits(num)) # 4
