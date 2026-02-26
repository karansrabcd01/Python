'''Problem Statement: 
         Create a class “Programmer” for storing information of few programmers working at Microsoft.'''



#creating a class named Programmer
class Programmer:

    #this is a class variable
    #class variables is shared by all objects of tis class

    company= "Microsoft" #class variable (same for all objects or programmers in this case)

    # __init__ is a constructor
    # Constructor runs automatically when we create an object of the class 
    # It is used to initialize the attributes
    
    def __init__(self,name,salary,language):
        
        # Instance variables (unique for each object)
        #self.name stores the name of the programmer 
        # "self" refers to the current object of the objects of the class
        self.name=name

        #self.salary stores the salary of the programmer
        self.salary=salary

        #self.language store the programming language of the programmer
        self.language=language 

      #Creating a method to display progarmmer details 

    def get_info(self):

        # Printing company name using the class variable 
        print("company: ", Programmer.company)

        #Printing name of Programmer 
        print("Name:", self.name)

        # Printing salary of Programmer
        print("Salary:",self.salary)



        #Printing the programming language of the Programmer
        print("Programming Language:",self.language)

        #Line For Better output Formatting 

        print("-"*30)

# Creating the onjects (instances) for the Progrmmer class

# Each object represent one programmer

p1=Programmer("Karan",120000,"Python")

p2=Programmer("Kishlay",100000,"Java")

p3= Programmer("Vidhi",800000,"C++")


#calling method by using object
# This will Print info of Each Programmer

p1.get_info()
p2.get_info()
p3.get_info()





    