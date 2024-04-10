from functools import reduce
# Write a Python function calculate_factorial that takes an integer as 
# input and uses the reduce function to return the factorial of that number.
def calculate_factorial(num):
    temp=[i for i in range(1,num+1)]
    factorial=reduce(lambda x,y:x*y,temp)
    return factorial
print(calculate_factorial(5))

#Implement a function called concatenate_strings that takes a list of strings as input 
# and uses the reduce function to return a single string containing the concatenation of all the elements.
def concatenate_string(strings):
    return str(reduce(lambda x,y:x+y,strings))
print(concatenate_string(["Sachin","Acharya"]))
