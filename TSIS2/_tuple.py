''' CREATING A TUPLE '''
my_tuple = ("apple", "banana", "cherry", "apple")
print(my_tuple)
print(len(my_tuple))

''' CREATING TUPLE WITH ONE ITEM  '''
my_tuple = ("apple", )
print(type(my_tuple))# <class 'tuple'>
my_tuple1 = ("apple")
print(type(my_tuple1)) # <class 'str'>
# A tuple can contain different data types:
my_tuple = ("abc", 34, True, 40, "male")


''' THE TUPLE() CONSTRUCTOR '''
my_tuple = tuple(("apple", ))
print(my_tuple) # ('apple' ,)


''' ACCESS TUPLE ITEMS '''
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1]) # banana
print(my_tuple[-1]) # cherrry
print(my_tuple[2:5]) # ('cherry',)
print(my_tuple[:2]) # ('apple', 'banana')
print(my_tuple[1:]) # ('banana', 'cherry')
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(my_tuple[-4:-1]) # ('orange', 'kiwi', 'melon')

''' CHECK IF ITEMS EXISTS '''
my_tuple = ("apple", "banana", "cherry")
if "apple" in my_tuple:
    print("Yes, 'apple' is in the fruits tuple")

''' UPDATE TUPLES '''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# 1
my_tuple = ("apple", "banana", "cherry")
y = list(my_tuple)
y.append("orange")
my_tuple = tuple(y)

# 2 ADD TUPLE TO A Tuple
my_tuple1 = ("apple", "banana", "cherry")
y = ("orange", )
my_tuple1 += y
print(my_tuple1) # ('apple', 'banana', 'cherry', 'orange')

# 3 remove items
my_tuple = ('apple', 'banana', 'cherry', 'orange')
y = list(my_tuple)
y.remove("orange")
my_tuple = tuple(y)
del my_tuple # delete the tuple completely


''' UNPACK TUPLES '''
fruits = ("apple", "orange", "cherry", "strawberry")
(green, yellow, *red) = fruits
print(green) # apple
print(yellow) # banana
print(red) # ['cherry', 'strawberry']


''' LOOP TUPLE  '''
my_tuple = ('apple', 'banana', 'cherry', 'orange')
for x in my_tuple:
    print(x)

for i in range(len(my_tuple)):
    print(my_tuple[i])

i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1   


''' JOIN TUPLES '''
my_tuple1 = ('a', 'b', 'c')
my_tuple2 = (1, 2, 3)
my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3) # ('a', 'b', 'c', 1, 2, 3)
chars = my_tuple1 * 2
print(chars) # ('a', 'b', 'c', 'a', 'b', 'c')

