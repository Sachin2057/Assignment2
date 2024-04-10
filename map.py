# def convert(*args):
#     return list(map(lambda x: x.upper(),args))

#assert convert("Sachin","Acharya")==["SACHIN","ACHARYA"]

# Create a function convert_to_uppercase that takes a list of strings as input 
# and uses the map function to return a new list with all the strings converted to uppercase.
def convert_to_uppercase(strings):
    return list(map(lambda x:x.upper(),strings))
assert convert_to_uppercase(["Sachin","Acharya"])==["SACHIN","ACHARYA"]
assert convert_to_uppercase(["Sachin","Acharya","FuseMachines"])==["SACHIN","ACHARYA","FUSEMACHINES"]

# Write a Python function square_numbers that takes a list of integers
# as input and uses the map function to return a new list containing the square of each element.
def square_numbers(nums):
    return list(map(lambda x:x**2 ,nums))
print(square_numbers([1,2,3,4,5]))
