# module vs. objects: module is a file that can be imported/exported into other files. But similar to an object, in that it is its own entity that can be included within a larger program

# CLASSES & INSTANCES
# Classes define the blueconsole.log for an object - naming convention in Python is capitalize 1st letter 

# Instances are an actual copy of that blueconsole.log

# Important built-in function __init__ runs when a new instance of a class is created
    # this function is also called a constructor: a function that runs when we create something

    # first parameter of __init__ is called 'self' and refers to instance that's being created. This parameter is automatically supplied, no need to manually define

    # the other parameters will be initial variable values for the instance

class Pet: 
    # variables created here are called class variables - will stay the same throughout all class instances
    class_var = 100


    def __init__(self, name, pet_type, age):
        # instance variables
        self.name = name
        self.pet_type = pet_type
        self.age = age


# CREATING AN INSTANCE

my_pet = Pet('mushu', 'cat', 2)

print(my_pet.name)
print('testing')
