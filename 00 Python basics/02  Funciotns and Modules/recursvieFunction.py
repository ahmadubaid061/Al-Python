#recursive function means a function calling itself again and again
# lets see the funciton for calculating the fibunacci value of a numnbers n
# In fibonacci series each value is the sum of previous two numbers but it should be positive
# like 0,1,1,2,3,5,8
def fib(n):
    if(n==0 or n==1):
        return n
    return fib(n-2)+fib(n-1) 
''' here the funciton is again called twice for a value (n-1) and a value(n-2)
and this how it goes deep down untill the n-1 and n-2 or n is (1 or 0)

''' 
print(f"fibunacci value of 6 is: {fib(6)}")
''' how this works 
first the funciotn checks if the value is zero or 1 which is not
then the function is again called for value 
fib(6-2)+ fib(6-1)
=> fib(4)+fib(5)
=>again the fib(4) is broken into fib(2)+fib(3) and
  fib(5) is broken into fib(3)+fib(4) and this way the recusion continuos untill all 
  the values are eaither 0 or 1
=> fib(2)+fib(3)+fib(3)+fib(4)
=> fib(0)+fib(1)+fib(1)+fib(2)+fib(1)+fib(2)+fib(2)+fib(3)
    fib(0) reurns 0 and fib(1) reurns 1
    so
=> 0+1+1+fib(0)+fib(1)+1+fib(0)+fib(1)+fib(0)+fib(1)+fib(1)+fib(2)
=> 0+1+1+0+1+1+0+1+0+1+1+fib(0)+fib(1)
=> 0+1+1+0+1+1+0+1+0+1+1+0+1
=> final answer is 8
=> in fibonacci series the value at sixth index is 8 or simply
 the 7th term in fibonacci series is 8
'''
