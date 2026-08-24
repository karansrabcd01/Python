"""
🟢 Problem 1 — Personal Information
Difficulty

Easy

Topic

Input → Variables → Output

Problem

Write a program that takes a person's:

name
age
city

as input and prints their information in the following format:

Name: Karan
Age: 21
City: Delhi
Example 1

Input:

Karan
21
Delhi

Output:

Name: Karan
Age: 21
City: Delhi
Constraints
name is a string.
age is a positive integer.
city is a string.

"""
#Start

user_name=input("Enter Your Name: ")
user_age=int(input("Enter Your Age: "))
user_city_name=input("Enter Your City Name: ")

#the question asked in proper format so keep it in the mind 
# print("Your name is:",user_name)
# print("Your Age is:",user_age)
# print("Your City name is:",user_city_name) 



print("Name:",user_name)
print("Age:",user_age)
print("City:",user_city_name)