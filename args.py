# Write a Python function that takes an arbitrary number of positional arguments and returns the sum of all the numbers. 
# Test your function with various input cases.
def add(*args):
    return sum(args)
try:
    assert add(1,2,3,4,5) ==15
    assert add(4,5,6,7,8,9,10) == 49
    assert add(4,3,3) ==10
except AssertionError:
    print("There seems to be some problem")
# Write a Python function concat_strings that takes any 
# number of strings as arguments and returns a single concatenated string.
  
def concat_strings(*args):
    return "".join(i for i in args)

try:
    assert concat_strings("Fuse","Machines","Pvt","Ltd")=="FuseMachinesPvtLtd"
    assert concat_strings("Hello", "world")=="Helloworld"
except AssertionError:
    print("Error during test")
