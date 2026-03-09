#built in modules means pre defined libraries that include 
# funcitons we can use directly without defining them
''' 
just like math library

After importing the math module using import math, we can use numerous mathematical
functions and constants for operations ranging from basic arithmetic and trigonometry
to logarithms and special functions. 
Key functions include:
Number Theory/Representation: 
    ceil(x), floor(x), fabs(x), factorial(n), gcd(*ints), isqrt(n), trunc(x).
Power/Logarithms:
    pow(x, y), sqrt(x), exp(x), log(x, base), log10(x), log2(x).
Trigonometry (radians): 
    sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), atan2(y, x).
Conversion/Hyperbolic:
    degrees(x), radians(x), and functions for hyperbolic sine, cosine, and tangent (sinh, cosh, tanh, asinh, acosh, atanh).
Constants:
    pi, e, tau, inf, nan.
'''

import math
print(math.sqrt(4))  # prints 2.0
#we have not defined the sqrt funtion but that is pre defined in the math library that we imported 

print(math.floor(5.6)) #prints 5
print(math.pow(2,3)) # means 2 raise to power 3
print(math.sin(0)) # 0.0
print(math.radians(60)) # converts 60 degree to radians 1.04719755...
print(math.pi) # prints value of pi = 3.14....