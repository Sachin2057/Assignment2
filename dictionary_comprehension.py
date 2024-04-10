#Given two lists
#one containing keys and another containing values, create a dictionary using dictionary comprehension.

def dictionary_compreshension(key,value):
    try:
        assert len(key)==len(value)
        return {
        key[i]:value[i] for i in range(len(key)) 
        }
    except AssertionError:
        print("Please enter eqaul len of keys and values")
    
print(dictionary_compreshension([1,2,3,4,5],[6,7,8,9,10]))

#Create a dictionary using dictionary comprehension to represent the 
# ASCII values of lowercase alphabets (a-z) where the keys are the alphabets, and the values are their corresponding ASCII values.
def ASCII():
    return {
        chr(i):i for i in range(97,123)
    }
print(ASCII())

# Given a dictionary with students' names as keys and their 
# respective scores as values, create a new dictionary that contains only the students who scored more than 80 using dictionary comprehension.
def passMarks(dictionary):
    return{
        i:j for i,j in dictionary.items() if j>80 
    }
print(passMarks({"Johnson":35,"Sachin":85,"Anup":45,"Pragyan":95}))