# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Demonstration of Exception Handling
#              Demonstration of Pickling
#
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PMcGiffin, 5.31.22, Code to complete Assignment 07
# ------------------------------------------------------------------------ #

# Pickling and unpickling data
# Saving to a serialized file format that can be retrieved.

import pickle # importing pickle

# Pickle methods
# pickle.dump() data type -- > serialized
# pickle.dumps() (from bit string)
# pickle.load() serialized -- > data type
# pickle.loads() (from bit string)
print("************ Pickling in Python ****************")
example_dict = {1: "example1", 2: "example2", 3: "example3"} #Creating an example dictionary

pickle_out = open("dict.pickle","wb") # creating pickle method
pickle.dump(example_dict, pickle_out) #dumping data in pickle and parsing through dictionary
pickle_out.close()

pickle_in = open('dict.pickle', 'rb') # pulling data through pickle method.
example_dict = pickle.load(pickle_in) # loading data from pickle

print(example_dict) # printing data
print(example_dict[2]) # printing data index 2 to demonstrate data has not changed.

# Demonstrating pickling works
class example_class:  # creating classes
    a_number = 92
    a_string = 'hello_world'
    a_list = [1, 2, 3]
    a_dict = {'first': 'a', 'second': 2, 'third': [1,2,3]}
    a_tuple = (22, 33)

my_object = example_class()
my_pickled_object = pickle.dumps(my_object)
print(f"This is my pickled object: \n{my_pickled_object}\n")

my_object.a_dict = None

my_unpickled_object = pickle.loads(my_pickled_object)
print(
    f"a_dict of unpickled object:\n{my_unpickled_object.a_dict}")

print("************ Exception Handling ****************")
# Error/Exception handling
# try:
#     f = open('testfile.txt')
# except Exception:
#     print('Sorry, this file does not exist')



# try:
#     # Runs code first
#     < code >
# except:
#     # Runs this if exception occurs in the try block
#     < code >
# else:
#     # Executes if the try block succeeds
#     < code >
# finally:
#     # This code will always execute
#     < code >

# Here is an example of exception handling:

try:
    a = int(input("Enter a value for a: "))
    b = int(input("Enter a value for b: "))
    c = a/b
    print("a/b = %d"%c)
except Exception:
    print("can't divide by zero")