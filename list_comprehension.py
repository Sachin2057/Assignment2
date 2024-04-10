# Given two lists of integers, create a list that contains the 
# product of each element of the first list with the corresponding element in the second list using list comprehension.
def multiplication(list1,list2):
    try:
        assert len(list1)==len(list2)
        return [list1[i]*list2[i] for i in range(len(list1))]
    except AssertionError:
        print("Please insert list of same length")


# Given a list of strings, create a new list that contains only the strings with more than 5 
# characters using list comprehension.
def string(words):
    return [i for i in words if len(i)>5]
print(multiplication([1,2,3,4,5],[3,4,5,6,0]))
