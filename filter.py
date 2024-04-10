# Write a Python function filter_long_strings that takes a list of strings as 
# input and uses the filter function to return a new list containing strings with more than 5 characters.
def filter_long_strings(stringList):
    return list(filter(lambda x:len(x)>5,stringList))
assert filter_long_strings(stringList=["Fuse","Machines"])==["Machines"]


# Implement a function called filter_prime_numbers that takes a list of integers as input and uses 
# the filter function to return a new list containing only the prime numbers.
def isPrimeNumber(num):
    if(num==1):
        return False
    elif(num<=3):
        return True
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
def filter_prime_numbers(nums):
    return list(filter(lambda x: isPrimeNumber(x),nums))

print(filter_prime_numbers([1,2,3,4,5,6,7,9,13]))