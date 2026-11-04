# Datetime
# import datetime

# x = datetime.datetime.now()
# # print(x.year)
# print(x.day)
# print(x.strftime("%Y"))

# Math

# x = min(5, 10, 25,-2)
# y = max(5, 10, 25)

# print(x)
# print(y)

# print(abs(5))

# print(pow(4,3))

import math

# print(math.sqrt(4))

# print(math.ceil(1.6))
# print(math.floor(1.9))

# print(math.pi)

# prices = [3000,1000,2000]
# print(sum(prices))
# rint(sum(3,5))

# JSON
# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# print(json.dumps(x))

# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)
# print(type(y))

# # the result is a Python dictionary:
# print(y["age"])

# Try Except
# print(x)
# print("Good morning")

# x = 5
# try:
#     print(x)
# except:
#     print("Name is not defined")
# else:
#     print("x is defined")
# finally:
#     print("The program is done")
    

# Raise an exception
# def calculate_total(price,quantity):
#     if price < 0:
#         raise ValueError("Price can't be negative")
#     if quantity <= 0:
#         raise ValueError("Quantity must be postive")
#     return price * quantity

# try:
#     total = calculate_total(-4,0)
# except ValueError as error:
#     print(error)
    
# Virtual Environment

# import numpy

# arr = numpy.array([1, 2, 3, 4, 5])

# print(arr)'

thisdict = {
    "brand":"Ford",
      "model": "Mustang",
  "year": 1964
}

del thisdict
# x = thisdict["model"]  #Read
# thisdict["color"] = "reds" #Create
# thisdict["year"] = 2026  #Update
# thisdict.pop()


# print(thisdict)