print("This is a test for python!")
print("This is a test 2 for python!")
print(5)
print(True)
print("$#@")
print("Hello World!")  # This line of code will print out Hello World!
# This line of code
#  will print out Hello World!
"""
This line of code
will print out Hello World!
"""
# print("Hello World!")

x = 5
y = 'Apple'  # No spaces between the variable name
z = 3.14  # we can not use - in variable name
_X2 = 5
a = False

print(x)
print(y)
print(z)
print(_X2)
print(a)
print(_X2, y, z)
print(type(x))
print(type(y))
print(type(z))
print(type(_X2))
print(type(a))

# 2x = 5  # We can not use a number as first char in name of variable

a, b, c = 5, 25, 50
print(a)
print(b)
print(c)
print(a + b + c)
print(type(a))
print(type(b))
print(type(c))

d = e = f = 50
print(d)
print(e)
print(f)
print(d + e + f)
print(type(d))
print(type(e))
print(type(f))

g = 5
h = 25
i = g + h
j = g - h
k = g * h
l = g / h

print(i)
print(type(i))
print(j)
print(type(j))
print(k)
print(type(k))
print(l)
print(type(l))

m = 5.5
n = 25

print("The addition of m & n is:", m + n)

o = 'hello'
print(o)

p = '''
This line of code
will print out Hello World!
'''
print(p)

q = 'Hello World!'
print(q[0:5])
print(q[0:])
print(q[6:9])
print(q[:5])
print(q.upper())
print(q.lower())

r = 'Hello'
s = 'World!'
print(r + s)
print(r + ' ' + s)

# 1. List [], 2. Tuple (), 3. Sets {}, 4. Dictionaries {}

list1 = ["Apple", "Banana", "Cherry"]
print(list1)
print(len(list1))
print(type(list1))
print(list1[1])
print(list1[-1])
print(list1[0:2])
print(list1[:2])
print(list1[1:2])

list1.append("Kiwi")
print(list1)

list1.insert(1, "Orange")
print(list1)

list1.remove("Banana")
print(list1)

list1.clear()
print(list1)

list2 = ["Apple", "Banana", "Cherry"]
list2.sort()
print(list2)

list3 = [5, 2, 55, 100, 1, 3, 80, 90, 66]
list3.sort()
print(list3)

list3.sort(reverse=True)
print(list3)

list4 = list3.copy()
print(list4)

list5 = list3 + list4
print(list5)

tuple1 = ("Apple", "Kiwi", "Banana", "Cherry")

print(tuple1)
print(len(tuple1))
print(type(tuple1))
print(tuple1[2])
print(tuple1[1])

x = list(tuple1)
x[1] = "Orange"
tuple1 = tuple(x)
print(tuple1)

y = list(tuple1)
y.insert(1, "Granberry")
tuple1 = tuple(y)

print(tuple1)
print(type(tuple1))

y.remove("Granberry")
tuple1 = tuple(y)
print(tuple1)

set1 = {"Apple", "kiwi", "Banana", "Cherry"}

print(set1)
print(len(set1))

set1.add("Orange")
print(set1)
print(len(set1))

#set1.remove("banana")
print(set1)
print(len(set1))

for x in set1:
    print(x)

set2 = {1, 2, 3}
set3 = set.union(set2)
print(set3)

set1.update(set2)
print(set1)

dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(dict1)
print(dict1["brand"])
print(dict1["model"])
print(dict1["year"])
print(len(dict1))
print(type(dict1))

x = dict1.keys()
print(x)

y = dict1.values()
print(y)

a = dict1.items()
print(a)

dict1.update({"year": 2022})
print(dict1)

dict1["Color"] = "Red"
print(dict1)

dict1.update({"Color": "Red"})
print(dict1)

dict1.pop("year")
print(dict1)

# If Else Statements
num = 2

if num == 0:
    print("Number is Zero")
elif num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# Loops in Python
i = 1

while i < 11:
    print(i)
    i += 1

for i in range(11):
    print(i)

num = 5

for x in range(11):
    print(num * x)


# Functions
def add(num1, num2):
    sum = num1 + num2
    return sum


print(add(5, 10))


def greet(name):
    print("Hello, how are you", name)


greet("John")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", add(num1, num2))

x = 5
try:
    print(x)
except Exception as e:
    print("An exception occurred:", e)

f = open("data.txt", "w")
f.write("Hello, this is a test file.")
f.close()

import os
import datetime
from time import sleep


os.remove('teste.txt')
time = datetime.time

while True:
    print(time)
    sleep(1)
