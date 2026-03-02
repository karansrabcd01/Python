'''Problem Statement: 
           Add a static method in problem 2, to greet the user with hello.

'''
# Creating the class name Calculator 

class Calculator:
    # Constructor method 
    # It Runs automatically when object is created
    # It initializes the number given by user 

    def __init__(self,number):
        
        #Instance variable to store the number 
        self.number=number

    # Method to calculate the square of the number

    def square(self):

        #Formula : Number * Number
        return self.number *self.number
    
    # Method to Calculate the cube of the number 
    def cube(self):

        #Formula : Number * Number * number
        return self.number*self.number*self.number

    # Method to Calculate the square root of the number 
    def square_root(self):

        # Formula : Number **0.5
        return self.number**0.5
    

    #Static method to greet the user
    @staticmethod
    def greet():
        """
        Static Method:
        --------------------
        - Does NOT use 'self'
        - Does NOT depend on object data
        - Belongs to the class

        It is used for utility/helper purposes.
        
        """
        print("Hello! Welcome to the Calculator. ")

    




# Calling static method Without creating onject
Calculator.greet()


# Creating the object for the calculator class
# Here we are passing the number 25

num1=Calculator(25)

#Calling method using object

print("Number:", num1.number)

# Calling the square method 

print("Square:", num1.square())

# Calling the Cube method 

print("Cube:", num1.cube())

#Calling the square root method

print("Square root:",num1.square_root())




