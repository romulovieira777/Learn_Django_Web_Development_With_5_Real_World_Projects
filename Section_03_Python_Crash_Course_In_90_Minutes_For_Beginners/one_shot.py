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

# 1. List, 2. Tuple, 3. Sets, 4. Dictionaries

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
