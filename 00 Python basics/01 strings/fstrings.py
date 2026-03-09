#f strings are used to print variable values inside double quotes easily
# suppose i want to print table of 2

# normally we do
for i in range(1,11):
    print("2 *",i," = ",2*i)


#but with f strings we can also do like
for i in range(1,11):
    print(f"2 * {i} = {2*i}")