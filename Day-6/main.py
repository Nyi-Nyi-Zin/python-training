# Match Statment
# day = 10
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _:
#     print("Looking forward to the Weekend")
    
# Combine Values
# day = 1
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Today is a weekday")
#   case 6 | 7:
#     print("I love weekends!")
    
# If Statements as Guards
# month = 20
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month == 4:
#     print("A weekday in April")
#   case 1 | 2 | 3 | 4 | 5 if month == 5:
#     print("A weekday in May")
#   case _:
#     print("No match")

# While Loops

# i = 1
# while True:
#   print(i)
#   i += 1

# break Statement
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# print("i is no longer less than 6")

# range() Function
# for x in range(6):
#   print(x)

# for x in range(2, 6):
#   print(x)

# for x in range(2, 30, 3):
#   print(x)

# Nested Loops
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# Functions
# def my_function():
#     print("Hello")
    
# my_function()
# my_function()
# my_function()

# Return Values
# def greeting():
#     return "Hello from a function"

# message = greeting()
# print(message)

# Parameters and Arguments

# def my_function(name):
#   print("Hello", name)

# my_function("Emil")

# Default Parameter Values
# def my_function(name = "friend"):
#   print("Hello", name)

# my_function("kyaw")

# Keyword Arguments
# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function("dog","buddy")

# *args, **kwargs
# def my_function(*kids):
#   print("The youngest child is " + kids[0])

# my_function("Emil", "Tobias", "Linus")

# Scope
# def myfunc():
#   x = 300
# #   print(x)
  
# print(x)

# Global Scope
# x = 300

# def myfunc():
#   print(x)

# myfunc()

# print(x)

# Add List Items
# thislist = ["apple","banana","cherry"]
# thislist.append("orange")
# print(thislist)

# Insert Items
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2,"orange")
# print(thislist)

# Extend List
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# Remove List Items
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("cherry")
# print(thislist)

# Python Module
def greeting(name):
  print("Hello, " + name)