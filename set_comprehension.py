# Given a list of numbers, create a set using set 
# comprehension that contains only unique even numbers.
def unique_even_numbers(list1):
    return {i for i in list1 if i%2==0}
print(unique_even_numbers([1,2,2,3,4,5,6]))

# Given a list of words, write a Python program to create a set using set comprehension that contains all
# the unique characters present in the words.
def unique_characters(words):
    return {j for i in words for j in i}
print(unique_characters(["Hello","World"]))

#Given two strings, write a Python program to create a set using set comprehension that contains all 
#the characters that are common in both strings.
def common_characters(string1,string2):
    return {j for j in string1 if string2.count(j)>0}
print(common_characters("Fuse" ,"Machines"))