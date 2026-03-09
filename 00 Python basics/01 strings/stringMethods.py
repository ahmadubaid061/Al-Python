#strings are immutable (cannot be change
#suppose
mystr="hello world"
# i cannot do as mystr[0]='a'
#upper() and Lower()
print(mystr.upper())
print(mystr.lower())

# strip()
# this function removes all the newline charactors and spaces from start and end of a string
name="  Ubaid Ahmad "
print(name.strip())  #prints "Ubaid Ahmad"
print(name.lstrip()) # removes spaces only from left(start) side
print(name.rstrip()) # removes spaces from right(end) side 

#find and replace
print(name.find("U")) # returns index of first appearance of U in the name
print(name.replace("Ahmad","GUl")) # replaces Ahmad with GUL

#split() and join()
stringX="My,name,IS,Ubaid,Ahmad"
print(stringX.split(',')) #splits the string into multiple items and that are in the form of a list of strings
#  ['My', 'name', 'IS', 'Ubaid', 'Ahmad'] we can store this in a variable
listX=stringX.split(',')

#join()
# with join we can convert a list into a single long string by definig a joining characotr like in list a 'space' is used
listY=['welcom','TO','Python'] # a list with 3 strings 
strY=' '.join(listY)
print(strY) # welcom TO Python


#Boolean functions
#isalpa() isdigit() isnum() isspace()
stringz="abc 123"
print(stringz.isalpha()) # if all charactors are alphabets so false
print(stringz.isdigit()) #if all charactors are digits  so alse
print(stringz.isalnum()) #if all characots are alphabets or digits so false
print(stringz.isspace()) #if all charctors are spaces so false
