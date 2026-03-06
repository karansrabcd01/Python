"""
Problem Statement:-
Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects.

"""

class Student:

    #constructor with "slf" instead of "self"
    def __init__(slf,name,marks):
        slf.name=name
        slf.marks= marks

    # Instance method using "slf"
    def display(slf):
        print("Name:",slf.name)
        print("Marks:",slf.marks)

#Creating Object
s1=Student("Abhishek",95)
# Calling Method
s1.display()

class Teacher:

    #Constructor using "Harry"
    def __init__ (harry, subject , salary ):
        harry.subject=subject
        harry.salary=salary

    #instances Method s=using "harry"
    def info(harry):
        print("Subject:",harry.subject)
        print("salary:",harry.salary)


#Creating Object
t1=Teacher("Python",100000)

#Calling method
t1.info()



