''' Creating '''
x = 5
y = "Nursat"
print(x) # 5
print(y) # Nursat

x = 4
x = "Sally"
print(x) # Sally 


''' Casting '''
x = str(3) # '3'
y = int(3) # 3 
z = float(3) # 3.0

''' Get the type '''
x = 5
y = "Nursat"
print(type(x))  # <class 'int'> 
print(type(y))  # <class 'str'>

''' Single or Double quotes '''
x = "Nursat"
# is the same as
x = 'Nursat'

''' Case-Sensitive '''
a = 4
# A will not overwise a
A = "Nursat"

''' Variable names '''
myname = "Nurrsat"
my_name = "Nursat"
myname2 = "Nursat"
MYNAME = "Nursat" 

''' MUlti words Variable names '''
# Camel case
myVariableName = "John"
# Pascal Case 
MyVariableName = "John"
# Snake case
my_variable_name  = "John"

'''Assign Multiple Values '''
# Many values to multiple variable
x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry

# One value to multiple variable
x = y = z = "Cherry"
print(x) # Cherry
print(y) # Cherry
print(z) # Cherry

# Unpack a colecition
fruits = ["apple", "banana", "cherry"]
x = y = z = fruits
print(x) # apple
print(y) # banana
print(z) # cherry\
 
''' Unpacking a Tuple '''
fruits = ("apple", "banana", "cherry")
# Using Asterisk ***********
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow,*red) = fruits
print(green) # apple
print(yellow) # banana
print(red) # ['cherry', 'strawberry', 'raspberry']
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow,red) = fruits
print(green) # apple
print(yellow) # ['banana','cherry', 'strawberry']
print(red) # raspberry

''' OUTPUT VARIABLE '''
x = " Python is awesome "
print(x)
x = "Python"
y = 'is'
z = "awesome"
print(x,y,z) # Python is awesome
x = 5
y = 10
print(x + y) # 15
x = 5
y = "Nursat"
print(x, y)

''' GLOBAL VARIABLE '''
x = "awesome"

def function():
    print("Python is " + x)

function() # Python is awesome

def function_2():
    x = "fantastic" # x is the local variable
    print("Python is :" + x)

function_2() # Python is fantastic
print( "Python is " + x) # Python is awesome

# The global Keywords 
x = "awesome"

def function_3():
    global x
    x = "fantastic"
    print("Python is " + x)

function_3() # Python is fantastic
print("Python is " + x) # Python is fantastic