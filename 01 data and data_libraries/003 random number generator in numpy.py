#numpy provide a random number generator funciton which generates random numbers 

import numpy as np

rng=np.random.default_rng() #creating the object
flips=rng.integers(0,2,size=100) #means create a list of size 100 and the elements should be either 0 or 1 (in range of 0:2)
probablitiyOfheads=np.mean(flips) 

print("Estimated probability of heads: ",probablitiyOfheads) #should be different each time

# printing the list of random numbers
for item in flips:
    print(item ,end=" ")