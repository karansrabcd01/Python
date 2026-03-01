''' Problem Statement:
Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?

'''

# Creating the class 

class Test:

    # This is the class attributes (class veriable )
    # It belongs to the class , not to individual object

    a=10


# Creating the object of class Test

obj=Test()

# Printing the class attribute using class name 

print(" Class attributes before Change:",Test.a)

# Printing class attributes using object

print("Object accessing class attributes", obj.a)

# Now Setting 'a' directly using object

# This does not change the class attributes 

# Instead it creates a new instance variable inside obj

obj.a=0

# Printing Values after modification

print("Object attributes after change :", obj.a)

# # Printing Class atributes again

print("Class attributes after change :", Test.a)
