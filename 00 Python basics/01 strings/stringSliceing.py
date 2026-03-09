# by slicing we can store some part of a string in a variable or directly print that
name='Ubaid Ahmad'
firstName=name[0:5]  #starts from index 0 and ends before 5
print(firstName)  #this will print Ubaid

lastName=name[6:]  #takes all the charactors after index 6 includeing 6
print(lastName)
#also
print(name[:6])# it will print from index 0 to 6-1

#we can also use negative indexing
name1=name[0:-6]
print(name1)  #it will also print Ubaid

#skipping some charactors
#for that a third parameter is used

name2=name[0:12:2] # the third parameter means skip(2-1)charactor after each charactor
print(name2)  # this print UadAmd
print(name[0:12:6]) # this will skip (6-1) charactors after each value and prints "UA" 
