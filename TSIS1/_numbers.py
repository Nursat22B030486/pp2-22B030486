# PYTHON NUMBERS
'''
There are three numeric types in Python:
   -> int
   -> float
   -> complex

'''
x = 5 # int
y = 2.8 # float
z = 1j # complex

#To verify the type of any object in Python, use the type() function:
x = 10
print(type(x)) # <class 'int'> 

# INT - is whole number, positive or negative, without decimals, of unlimited length
x = 1
y = 65465413219845163498
z = -3546546
print(type(x)) # <class 'int'>
print(type(y)) # <class 'int'>
print(type(z)) # <class 'int'>

# Float - is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59
a = 35e3
b = 12E4
c = -87.7e6545
print(type(x)) # <class 'float'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'float'>
print(type(a)) # <class 'float'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'float'>

# COMPLEX numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j
print(type(x)) # <class 'complex'>
print(type(y)) # <class 'complex'>
print(type(z)) # <class 'complex'>

'''  TYPE CONVERSION '''
x = 1
y = 2.8
z = 1j
#convert from int to float
a = float(x)
#convert from float to int
b = int(y)
#convert from int to complex
c = complex(x)
print(a) # 1.0
print(b) # 2
print(c) # 1+0j
print(type(a)) # <class 'float'>
print(type(b)) # <class 'int'>
print(type(c)) # <class 'complex'>
####### WE CANNOT CONVERT COMPLEX NUMBERS INTO ANOTHER NUMBER TYPE
''' RANDOM NUMBER '''
import random
print(random.randrange(1, 10)) 