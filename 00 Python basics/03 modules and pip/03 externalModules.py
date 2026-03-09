#external modules are libraries that we can install in our compiler 
# using terminal commond pip install module_name

#such as requests 

#we can run in terminal (pip install requests)
#requests are generally used for getting html code of a website using the get() funciton

import requests  #i have already install the requests module

r=requests.get("https://pypi.org/project/requests/") 
#the get() funciton is predefined funciton in requests 
# module to fitch html code from a website url

print(r.text ) # this prints all the html code in text format

# there are alot other external modules that we cacn install and import using pip 
