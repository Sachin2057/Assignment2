# Write a Python function calculate_total_cost that calculates the total cost of items 
# purchased from a store. The function should accept multiple keyword arguments, where the key is the item name, and the value is the item's price. The function should return the total cost of all items.
def calculate_total_cost(**kwargs):
    return sum(kwargs.values())
try:
    assert calculate_total_cost(apple=100,orange=200,mang0=500) == 800
    assert calculate_total_cost(jam=500,chips=50)==550
    assert calculate_total_cost(momo=150) ==150
except AssertionError:
    print("There seems to be some problem in test or code")

# Create a function create_student_report that takes the student's name as the first argument, the student's age as the second argument, and an arbitrary number of keyword arguments for the subjects and their respective scores. The function should return a 
# dictionary with the student's information and a list of subjects along with their scores.
def create_student_report(name,age,**kwargs):
    return {
        "Name":name,
        "Age":age,
        "Subjects":kwargs
    }
print(create_student_report("Sachin", 23, Math=85, Science=90, History=75))