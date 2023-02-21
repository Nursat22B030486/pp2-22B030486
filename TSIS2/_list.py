mylist = ["apple", "banana", "cherry"]
print(mylist)

''' ALLOW DUPLICATES '''
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # ['apple', 'banana', 'cherry', 'apple', 'cherry']

''' LIST LENGTH '''
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3

''' LIST ITEMS - DATA TYPES '''
list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3, 4, 5, 6]
list3 = [True, False, False]
# list can contain different data types:
list1 = ["abc", "34", True, 40, "male"]
print(type(list1)) # <class 'list'>

''' THE list constructor '''
this_list = list(("apple", "banana", "cherry")) # note the double round-brackets
print(this_list) 

''' ACCESS LIST ITEMS '''
list1 = ["apple", "banana", "cherry"]
print(list[2]) # cherry
# negative indexing
print(list[-1]) # cherry
# range of indexes
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1[2:5]) # ['cherry', 'orange', 'kiwi']
print(list1[:4]) # ['apple', 'banana', 'cherry', 'orange']
print(list1[2:]) # ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(list1[-4:-1]) # ['orange', 'kiwi', 'melon']

''' CHECK IF ITEMS EXISTS '''
list1 = ["apple", "banana", "cherry"]
if "apple" in list1:
    print("Yes, 'apple' is in the fruits list")

''' CHANGE LIST ITEMS '''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print("thislist")
# change a Range of item values
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Change the second value by replacing it with two new value
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']
thislist = ["apple", 'banana', "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ['apple', 'watermelon']

''' INSERT ITEMS '''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"watermelon")
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry']

''' ADD LIST ITEMS '''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ['apple', 'banana', 'cherry', 'orange']
# extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

''' REMOVE LIST ITEMS '''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']
thislist.pop ()  # removes the last item
del thislist[0] # removes the specified index
del thislist # delete the list completely

''' Clear the list '''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # []

''' LOOP LISTS '''
thislist = ["apple", "banana", "cherry"]
# Loop Through a List
for x in thislist:
    print(x)  
[print(x) for x in thislist]
# Loop Through the Index Numbers
for i in range(len(thislist)):
    print(thislist[i])
# Using a While Loop
i = 0
while i <len(thislist):
    print(thislist[i])
    i += 1
''' LIST COMPREHENSION '''
# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
# or
newlist = [x for x in fruits if "a" in x]

''' The Syntax '''
# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in fruits]
newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]

''' SORT LIST ALPHANUMERICALLY '''
my_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
my_list.sort()
print(my_list) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
''' Sort Descending order '''
my_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
my_list.sort(reverse = True)
print(my_list) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
''' Customize Sort Function '''
def my_function(n):
    return abs(n-50)
my_list = [100, 50, 65, 82, 23]
my_list.sort(key = my_function)
print(my_list) # [50, 65, 23, 82, 100]
""" The SORT() method is case sensitive(Capital first).If you want sort except it, just use str.lower as a key function"""
''' reverce() order '''
my_list = ["banana", "Orange", "Kiwi", "cherry"]
my_list.sort()
print(my_list) # ['Kiwi', 'Orange', 'banana', 'cherry']
my_list.reverse() 
print(my_list) # ['cherry', 'Kiwi', 'Orange', 'banana']


''' COPY LIST '''
my_list = ["apple", "banana", "cherrry"]
copy_list = my_list.copy()
result = ", ".join(copy_list)
print(result)
# second way
my_list = ["apple", "banana", "cherry"]
result = list(my_list)
print(result)

''' JOIN LISTS '''
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
# 1-way
list3 = list1 + list2
print(list3)
# second way
for x in list2:
    list1.append(x)
print(list1)
# third way
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
